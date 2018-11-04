# Trabalho TCP 2018/2
from __future__ import print_function
import numpy as np
import os
import pyaudio
import wave
import sys
import librosa
import soundfile as sf

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

def mapeia(char, cont, volume, bpm, stringNova, stringNova2):
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
        elif char == 'H' or char == 'h':
            stringNova, stringNova2 = criaNovoWav(stringNova2, stringNova, cont, volume, bpm)
        else:
            stringNova, stringNova2 = criaNovoWav("../Pasta_dos_Arquivos/silence2.wav",'../Pasta_dos_Arquivos/novo_silence.wav',cont, volume, bpm)

    return cont, volume, bpm, stringNova, stringNova2

def criaNovoWav(string, novo_nome, num, volume, bpm):
    y, sr = librosa.load(string)
    new_wav = librosa.effects.pitch_shift(y, sr, num) # cria um array novo com a oitava definida
    new_wav = new_wav[:] * (volume)
    # librosa.output.write_wav(novo_nome, new_wav, sr)
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    print(tempo)
    sf.write(novo_nome, new_wav, 100*bpm, 'PCM_24')
    tocaMusica(novo_nome)
    return novo_nome, string


def tocaMusica(string):
    wf = wave.open(string, 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

    data = wf.readframes(CHUNK)

    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)
        # print(data)

    stream.stop_stream()
    stream.close()

    p.terminate()
    # return stringNova

def main():
    t = Texto("AAAAAAAAAAAAAA;;;;;;;;;;;;;;;;;;;;;;;;;;;AAAAAAAAAAA;;;;HHHHHHHHHHHHH;;;;;AAAAA,,,,,,,,,AAAAAAAAAAAAA,,,,,,,,AAAAAAAAAAAAAA,,,,AAAAAAAAA,,,,,,,BBBBBBBBBB,,,,,,BBBBBBBBB,,,,,BBBBBBBB")
    t.geraTXT()

    with open('saida.txt') as f:
        data = f.read()

    # Mandar cada letra do texto para a função Mapeia
    x = 0
    vol = 1
    bpm = 120
    defaultString = ""
    defaultString2 = ""
    for i in data:
        x, vol, bpm, defaultString, defaultString2 = mapeia(i, x, vol, bpm, defaultString, defaultString2)


if __name__ == '__main__':
    main()
