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


CHUNK = 1024

# classe Tratamento de Texto
class Texto:
    """Classe que gera o .txt com o texto digitado"""
    def __init__(self, texto): # Construtor
        self.txt = texto

    def geraTXT(self):
        """Gera arquivo saida.txt."""
        self.f = open('saida.txt', 'w')
        self.f.write(self.txt)
        self.f.close()

class GerenciaMusica:
    def load(self, string, oitava):
        y, sr = librosa.load(string) # Carrega Antigo WAV
        new_wav = librosa.effects.pitch_shift(y, sr, oitava) # cria um array novo com a oitava definida num => cont(oitava)
        return y, sr, new_wav

    def hz_to_MIDI(self, varMidi, varMusica): # Conversão de HZ para notas MIDI
        y , sr, new_wav = self.load(varMusica.getAntigoWav(), varMusica.getOitava())
        tempo, beats = librosa.beat.beat_track(onset_envelope = new_wav[:200], sr=sr)
        varMusica.GeneralMIDI = librosa.hz_to_midi(tempo)

        print("varMusica general Midi {}".format(varMusica.GeneralMIDI))
        varMidi.funcao_do_midi(varMusica.GeneralMIDI)
        self.criaWav('file3.wav', 'novissimo.wav', varMusica)

    def criaWav(self, new_wav, novo_nome, varMusica):
        y, sr, new_wav = self.load(new_wav, varMusica.getOitava())
        sf.write(novo_nome, new_wav, sr, 'PCM_24')
        self.tocaMusica(novo_nome)

    def tocaMusica(self, string):
        #open a wav format music
        wf = wave.open(string, 'rb')
        #instantiate PyAudio
        p = pyaudio.PyAudio()

        #open stream
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True)

        #read data
        data = wf.readframes(CHUNK)

        #play stream
        while data != b'':
            stream.write(data)
            data = wf.readframes(CHUNK)
            # print(data)

        stream.stop_stream()
        stream.close()

        p.terminate()
        # return stringNova


class Midi:
    """Classe Midi"""
    name = ""
    track = 0
    time = 0
    channel = 0
    volume = 0
    duration = 0
    MIDINOTE = 0

    def __init__(self, name, track, time, channel, volume, duration): #Construtor
        self.name = name
        self.duration = duration
        self.volume = volume
        self.channel = channel
        self.time = time
        self.track = track

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
        return self.volume

    def getChannel(self):
        return self.channel

    def getTime(self):
        return self.time

    def getDuration(self):
        return self.duration

    def funcao_do_midi(self, notas):
        mf = MIDIFile(1) # create my MIDI file
        mf.addTrackName(self.track, self.time, self.name)
        mf.addTempo(self.track, self.time, 120) #120 bpm
        self.MIDINOTE = notas
        # Cria .mid com a nota vinda do parametro
        mf.addNote(self.track, self.channel, int(notas), self.time, self.duration, 127) #Coloca Nota musical no arquivo
        with open(self.name, 'wb') as outf:
            mf.writeFile(outf)

        # cria .wav com o nome do parametro (vindo do terminal)
        spec = importlib.util.spec_from_file_location("__main__", "../PySynth/readmidi.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

# Musica => Midi
class Musica(Midi):
    """Classe Música"""
    bpm = 0
    antigoWav = ""
    novoWav = ""
    oitava = 0
    GeneralMIDI = Midi.MIDINOTE

    def __init__(self, bpm):
        self.bpm = bpm

    def setGenMIDI(self, nota):
        self.GeneralMIDI = nota

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