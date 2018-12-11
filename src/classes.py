#Módulo que reúne todas as principais classes e seus contrutores.

#importação de algumas bibliotecas para o funcionamento do programa
from __future__ import print_function
from midiutil.MidiFile import MIDIFile
import numpy as np
import os
import pyaudio
import wave
import sys
import librosa
import soundfile as sf
# Importar um módulo de outra pasta
import importlib.util

#Definição de uma constante
CHUNK = 1024

#classe que faz o tratamento de texto
class Texto:
    """Classe que gera o .txt com o texto digitado"""
    def geraTXT(self, texto):
        """Gera arquivo saida.txt."""
        self.txt = texto
        self.f = open('saida.txt', 'w')
        self.f.write(self.txt)
        self.f.close()
        return self.txt

#classe responsável pelo gerenciamento da musica
class GerenciaArquivos:

    #Método que carrega Antigo WAV e tranforma-o em um novo, de acordo com a leitura da string
    def load(self, string, oitava):
        y, sr = librosa.load(string) # Carrega Antigo WAV
        wav = librosa.effects.pitch_shift(y, sr, oitava) # cria um array novo com a oitava definida, wav = Antigo WAV
        return y, sr, wav

    #Conversão de HZ para notas MIDI
    def hz_to_MIDI(self, varMidi, varMusica):
        y , sr, wav = self.load(varMusica.getAntigoWav(), varMusica.getOitava())
        tempo, beats = librosa.beat.beat_track(onset_envelope = wav[:200], sr=sr)

        varMusica.GeneralMIDI = librosa.hz_to_midi(tempo)
        print("varMusica general Midi {}".format(varMusica.GeneralMIDI))
        varMidi.criaNovoMIDI(varMusica.GeneralMIDI)
        self.criaWav(sys.argv[3], 'novissimo.wav', varMusica)

    #Cria nova wav com as especifícações encontradas na string lida
    def criaWav(self, wav, final_wav, varMusica):
        y, sr, wav = self.load(wav, varMusica.getOitava())
        wav[:] = wav[:] * varMusica.getVolume() # Aumenta o volume ou incrementa em 10%
        sf.write(final_wav, wav, sr, 'PCM_24') #Função que cria o .wav em novo_nome
        self.tocaMusica(final_wav)

    #Método que irá tocar a música já configurada
    def tocaMusica(self, wav):
        #open a wav format music
        wf = wave.open(wav, 'rb')
        #instantiate PyAudio
        p = pyaudio.PyAudio()

        #open stream
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True)

        #read data
        data = wf.readframes(CHUNK)

        #play stream / tocando
        while data != b'':
            stream.write(data)
            data = wf.readframes(CHUNK)
            # print(data)

        stream.stop_stream()
        stream.close()

        p.terminate()
        # return stringNova

#Classe do MIDI
class Midi:
    """Classe Midi"""
    #Atributos Privados '__'
    midinote = 0

    #Contrutor do MIDI
    def __init__(self, name, track, time, channel, volume, duration): #Construtor
        self.name = name
        self.duration = duration
        self.volume = volume
        self.channel = channel
        self.time = time
        self.track = track

    #Define um novo arquivo com o formato MIDI
    def setNovo(self):
        self.midi = MIDIFile(1) # create my MIDI file
        self.midiTime = 0

    #Mais alguns construtores, setter's e getter's
    def setName(self, name):
        self.name = name

    def setDuration(self, duration):
        self.duration = duration

    def setVolume(self, volume):
        self.volume = volume

    def setChannel(self, channel):
        self.channel = channel

    def setTime(self, time):
        self.time = time

    def setTrack(self, track):
        self.track = track

    def getTrack(self):
        return self.track

    def getName(self):
        return self.Name

    def getVolume(self):
        return self.__volume

    def getChannel(self):
        return self.channel

    def getTime(self):
        return self.time

    def getDuration(self):
        return self.duration

    def addNoteToMidi(self, nota):
        '''Adicionando cada nota .mid ao .mid que vai conter todas as notas'''
        self.midi.addTempo(self.track, self.midiTime, 120) #120 bpm
        # Cria .mid com a nota vinda do parametro
        self.midi.addNote(self.track, self.channel, int(nota), self.midiTime, self.duration, 127) #Coloca Nota musical no arquivo
        self.midiTime = self.midiTime + 2

    #Setter do MIDI
    def setMIDI(self):
        with open('outmid2.mid', 'wb') as outf:
            self.midi.writeFile(outf)

    #Define o novo MIDI a ser salvo com as devidas configurações
    def criaNovoMIDI(self, notas):
        mf = MIDIFile(1) # create my MIDI file
        mf.addTrackName(self.track, self.time, self.name)
        mf.addTempo(self.track, self.time, 120) #120 bpm
        self.midinote = notas
        # Cria .mid com a nota vinda do parametro
        mf.addNote(self.track, self.channel, int(notas), self.time, self.duration, 127) #Coloca Nota musical no arquivo
        # Para Criar o BIG MIDI
        self.addNoteToMidi(int(notas))

        with open(self.name, 'wb') as outf:
            mf.writeFile(outf)

        # cria .wav com o nome do parametro (vindo do terminal)
        spec = importlib.util.spec_from_file_location("__main__", "../PySynth/readmidi.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

#Classe Musica que define alguns atributos inicias da música; Musica => Midi
class GerenciaMusica(Midi):
    """Classe Música"""
    bpm = 0
    antigoWav = ""
    novoWav = ""
    oitava = 0
    volume = 1
    GeneralMIDI = 0


    #Construtores, setter's e getter's da classe Musica
    def __init__(self, bpm):
        self.bpm = bpm

    def setGenMIDI(self, nota):
        self.GeneralMIDI = nota

    def doubleVolume(self):
        '''Dobra o volume'''
        self.volume = self.volume * 2

    def halfVolume(self):
        '''Corta o volume pela metade'''
        self.volume = self.volume / 2

    def IncrementVolume(self):
        '''Aumenta o volume em 10%'''
        self.volume = self.volume * (1.1)

    def getVolume(self):
        return self.volume

    def getGenMIDI(self):
        return self.GeneralMIDI

    def changeMIDI(self):
        return self.GeneralMIDI + 2

    def setWAV(self, antigoWav, novoWav):
        self.antigoWav = antigoWav
        self.novoWav = novoWav

    def setAntigoWav(self, antigoWav):
        self.antigoWav = antigoWav

    def setnovoWav(self, novoWav):
        self.novoWav = novoWav

    def setBPM(self, bpm):
        self.bpm = bpm

    def setOitava(self, oitava):
        self.oitava = oitava

    def getOitava(self):
        return self.oitava

    def getBPM(self):
        return self.bpm

    def getnovoWav(self):
        return self.novoWav

    def getAntigoWav(self):
        return self.antigoWav
