# Trabalho TCP 2018/2
from classes import *
# from TKinterface import *
from QtInterface import *


def mapeia(char, varMidi, varMusica):
    # print(char, "\n\n")
    varGerMusica = GerenciaMusica()
    # x = ord(char)                       # X é o numero ASCII do char se estiver entre 48 e 57 é um número
    if ord(char) >= 48 and ord(char) <= 57:             # É um número e agora vamos tirar o módulo para saber se é ímpar ou par
        varMusica.changeMIDI() # MIDI = MIDI + 2
    elif char == ' ':
        '''Char Espaço Dobra o Volume'''
        varMusica.doubleVolume()
    elif (char =='O' or char == 'o' or char == 'I' or char == 'i' or char == 'U' or char == 'u'):
        '''Aumenta o volume em 10%'''
        varMusica.IncrementVolume()
    elif char == '?' or char == '.':
        cont = 0
    elif char == ';':
        varMidi.funcao_do_midi() #???
    elif char == ',':
        varMidi.funcao_do_midi() #????
    elif char == 'A': #La
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/La.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_La.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == 'B': # Si
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Si.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Si.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == 'C': # Do
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Do.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Do.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == 'D': # Re
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Re.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Re.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == 'E': # Mi
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Mi.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Mi.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == 'F': # Fa
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Fa.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Fa.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == 'G': # Sol
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Sol.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Sol.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == 'a' or char == 'b' or char == 'c' or char == 'd' or char == 'e' or char == 'f' or char == 'g':
        '''Se vem esses caracteres toca a nota(.wav) que já esta armazenado na varMusica'''
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    elif char == '\n':
        varMidi.funcao_do_midi(53) #General MIDI 15 => 53
    elif char == '!':
        varMidi.funcao_do_midi(17)
    elif ord(char) >= 72 or ord(char) <= 90 or ord(char) >= 104 or ord(char) <= 122: # Qualquer consoante que não as notas
        varGerMusica.hz_to_MIDI(varMidi, varMusica)
    else: # Silêncio
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/silence.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_silence.wav')
        varGerMusica.criaWav('../Pasta_dos_Arquivos/novo_silence.wav', 'novissimo.wav', varMusica)


def main(args):
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())



def mapeia1(string):
    # print(string, "\n\n")

    t = Texto()
    t.geraTXT(string)
    # Colocar todas os caracteres do saida.txt no data
    with open('saida.txt') as f:
        data = f.read()

    varMidi = Midi("output.mid", 0, 0, 0, 100, 1)          #name, track, time, channel, volume, duration
    varMidi.setNovo()

    varMusica = Musica(120)
    varMusica.setOitava(12)
    # Mandar cada letra do texto para a função Mapeia
    for i in data:
        mapeia(i, varMidi, varMusica)

    # Cria o MIDI final (o BIGZÃO)
    varMidi.setMIDI()

if __name__ == '__main__':
    main(sys.argv)
