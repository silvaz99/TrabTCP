# Trabalho TCP 2018/2
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

class Musica:
    """Classe Música"""

class Midi:
    """Classe Midi"""
    name = ""
    track = 0
    time = 0
    channel = 0
    volume = 0
    duration = 0

    def __init__(self, name, track, time, channel, volume, duration):
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
        mf.addTempo(self.track, self.time, 120)
        # print(int(notas))
        mf.addNote(self.track, self.channel, int(notas), self.time, self.duration, self.volume)
        with open(self.name, 'wb') as outf:
            mf.writeFile(outf)

        spec = importlib.util.spec_from_file_location("__main__", "../PySynth/readmidi.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)



def mapeia(char, cont, volume, bpm, stringNova, stringNova2):
    import sys
    print(cont)
    x = ord(char)
    if x >= 48 and x <= 57: # É um numero e agora vamos tirar o módulo
        x = int(char)
        y = x % 2
        if y == 1:
            cont = cont - 1
        else:
            cont = cont + 1
    if char == '!':
        volume = volume*2
    elif (char =='O' or char == 'o' or char == 'I' or char == 'i' or char == 'U' or char == 'u'):
        volume = volume/2
    elif char == '?' or char == '.':
        cont = 0

    if char == ';':
        bpm = bpm + 50
    elif char == ',':
        bpm = bpm - 50

    else:
        if char == 'A' or char == 'a':
            stringNova, stringNova2 = criaNovoWav("../Pasta_dos_Arquivos/La.wav", '../Pasta_dos_Arquivos/novo_La.wav', cont, volume, bpm)
        elif char == 'B' or char == 'b':
            stringNova, stringNova2 = criaNovoWav("../Pasta_dos_Arquivos/Si.wav", '../Pasta_dos_Arquivos/novo_Si.wav', cont, volume, bpm)
        elif char == 'C' or char == 'c':
            stringNova, stringNova2 = criaNovoWav("../Pasta_dos_Arquivos/Do.wav", '../Pasta_dos_Arquivos/novo_Do.wav',cont, volume, bpm)
        elif char == 'D' or char == 'd':
            stringNova, stringNova2 = criaNovoWav("../Pasta_dos_Arquivos/Re.wav",'../Pasta_dos_Arquivos/novo_Re.wav',cont, volume, bpm)
        elif char == 'E' or char == 'e':
            stringNova, stringNova2 = criaNovoWav("../Pasta_dos_Arquivos/Mi.wav",'../Pasta_dos_Arquivos/novo_Mi.wav',cont, volume, bpm)
        elif char == 'F' or char == 'f':
            stringNova, stringNova2 = criaNovoWav("../Pasta_dos_Arquivos/Fa.wav",'../Pasta_dos_Arquivos/novo_Fa.wav',cont, volume, bpm)
        elif char == 'G' or char == 'g':
            stringNova, stringNova2 = criaNovoWav("../Pasta_dos_Arquivos/Sol.wav",'../Pasta_dos_Arquivos/novo_Sol.wav',cont, volume, bpm)
        elif char == '\n':
            funcao_do_midi(53)
        elif char == 'H' or char == 'h':
            stringNova, stringNova2 = criaNovoWav(stringNova2, stringNova, cont, volume, bpm)
        else:
            stringNova, stringNova2 = criaNovoWav("../Pasta_dos_Arquivos/silence2.wav",'../Pasta_dos_Arquivos/novo_silence.wav',cont, volume, bpm)

    return cont, volume, bpm, stringNova, stringNova2






def criaNovoWav(string, novo_nome, num, volume, bpm):
    y, sr = librosa.load(string)
    new_wav = librosa.effects.pitch_shift(y, sr, num) # cria um array novo com a oitava definida
    # new_wav = new_wav[:] * (volume) * 5
    # print(new_wav.size)
    tempo, beats = librosa.beat.beat_track(onset_envelope = new_wav[:100], sr=sr)
    print(tempo)
    # onset_env = librosa.onset.onset_strength(new_wav, sr=sr)
    # tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr, aggregate = None) # Estimate the tempo (beats per minute)
    # notas = librosa.hz_to_note(tempo)
    notas = librosa.hz_to_midi(tempo)
    print(notas)
    # x = notas.sum()/notas.size
    # funcao_do_midi(notas)
    return novo_nome, string

def funcao_tocaMusica(new_wav, novo_nome, num, volume):
    y, sr = librosa.load(new_wav)
    new_wav = librosa.effects.pitch_shift(y, sr, num) # cria um array novo com a oitava definida
    new_wav = new_wav[:] * (volume) * 10
    sf.write(novo_nome, new_wav, sr, 'PCM_24')
    tocaMusica(novo_nome)

def tocaMusica(string):
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

def main():
    t = Texto("A\nD")
    t.geraTXT()

    with open('saida.txt') as f:
        data = f.read()

    Musica = Midi("output.mid", 0, 0, 0, 100, 1)          #name, track, time, channel, volume, duration

    Musica.funcao_do_midi(53)
    funcao_tocaMusica('file3.wav', 'novoWav2.wav', 8, 1)

    # Mandar cada letra do texto para a função Mapeia
    x = 0
    vol = 1
    bpm = 120
    defaultString = ""
    defaultString2 = ""
    for i in data:
        x, vol, bpm, defaultString, defaultString2 = mapeia(i, x, vol, bpm, defaultString, defaultString2)

    # criaNovoWav("../PySynth/file3_B.wav",'../Pasta_dos_Arquivos/novoWAV.wav', 8, 1, bpm)



if __name__ == '__main__':
    main()
