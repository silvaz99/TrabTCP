# Trabalho TCP 2018/2
from __future__ import print_function
import os
import librosa

# classe Tratamento de Texto
class Texto:
    """Classe que gera o .txt com o texto digitado"""
    def __init__(self, texto): # Construtor
        self.txt = texto

    def geraTXT(self):
        """Gera arquivo saida.txt."""
        self.f = open('saida.txt', 'w')
        self.f.write(self.txt)

def main():
    t = Texto("Um texto\n")
    t.geraTXT()


if __name__ == '__main__':
    main()
