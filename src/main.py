# Trabalho TCP 2018/2
from __future__ import print_function
# import numpy as np
import os
import pyaudio
import wave
import sys
import librosa

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

def mapeia(char):
    # print(char)
    if char == 'A' or char == 'a':
        tocaMusica("../Pasta_dos_Arquivos/La.wav")
    elif char == 'B' or char == 'b':
        tocaMusica("../Pasta_dos_Arquivos/Si.wav")
    elif char == 'C' or char == 'c':
        tocaMusica("../Pasta_dos_Arquivos/Do.wav")
    elif char == 'D' or char == 'd':
        tocaMusica("../Pasta_dos_Arquivos/Re.wav")
    elif char == 'E' or char == 'e':
        tocaMusica("../Pasta_dos_Arquivos/Mi.wav")
    elif char == 'F' or char == 'f':
        tocaMusica("../Pasta_dos_Arquivos/Fa.wav")
    elif char == 'G' or char == 'g':
        tocaMusica("../Pasta_dos_Arquivos/Sol.wav")
    #else


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
        print(data)

    stream.stop_stream()
    stream.close()

    p.terminate()

def main():
    t = Texto("FGABCDGfEDcbAAbCdEfG\n")
    t.geraTXT()

    with open('saida.txt') as f:
        data = f.read()

    # Mandar cada letra do texto para a função Mapeia
    for i in data:
        mapeia(i)



if __name__ == '__main__':
    main()
