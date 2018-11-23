# Trabalho TCP 2018/2
from classes import *
# from TKinterface import *
from QtInterface import *


def mapeia(char, varMidi, varMusica):
    varGerMusica = GerenciaMusica()
    x = ord(char)                       # X é o numero ASCII do char se estiver entre 48 e 57 é um número
    if x >= 48 and x <= 57:             # É um número e agora vamos tirar o módulo para saber se é ímpar ou par
        varMusica.changeMIDI()

    if char == ' ':
        varMidi.volume = varMidi.volume*2
    elif (char =='O' or char == 'o' or char == 'I' or char == 'i' or char == 'U' or char == 'u'):
        varMidi.volume = varMidi.volume*(1.1)
    elif char == '?' or char == '.':
        cont = 0

    if char == ';':
        varMidi.funcao_do_midi() #???
    elif char == ',':
        varMidi.funcao_do_midi() #????
    elif char == 'A' or char == 'a': #La
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/La.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_La.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == 'B' or char == 'b': # Si
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Si.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Si.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == 'C' or char == 'c': # Do
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Do.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Do.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == 'D' or char == 'd': # Re
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Re.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Re.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == 'E' or char == 'e': # Mi
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Mi.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Mi.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == 'F' or char == 'f': # Fa
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Fa.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Fa.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == 'G' or char == 'g': # Sol
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Sol.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Sol.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == '\n':
        varMidi.funcao_do_midi(53) #General MIDI 15 => 53
    elif char == '!':
        varMidi.funcao_do_midi(17)
    elif char == 'H' or char == 'h':
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    else: # Silêncio
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/silence.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Silence.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)


def main(args):
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())



def mapeia1(string):
    t = Texto()
    t.geraTXT(string)
    # Colocar todas os caracteres do saida.txt no data
    with open('saida.txt') as f:
        data = f.read()

    varMidi = Midi("output.mid", 0, 0, 0, 100, 1)          #name, track, time, channel, volume, duration
    varMusica = Musica(120)
    varMusica.setOitava(12)
    # Mandar cada letra do texto para a função Mapeia
    for i in data:
        mapeia(i, varMidi, varMusica)


if __name__ == '__main__':
    main(sys.argv)
