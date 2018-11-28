# Trabalho TCP 2018/2
from classes import *
from QtInterface import *

# python3 main.py file.mid [tracknum] [file.wav]  [--syn_b/--syn_c/--syn_d/--syn_e/--syn_p/--syn_s/--syn_samp]


#Método que irá mapear cada caractere lido na string recebida pelo usuário em uma ação conforme o enunciado do trabalho
def mapeiaCaractere(char, varMidi, varMusica):
    # print(char, "\n\n")
    varGerMusica = GerenciaMusica()
    # ord() é o numero ASCII do char, se estiver entre 48 e 57 é um número
    if ord(char) >= 48 and ord(char) <= 57:
        varMusica.changeMIDI() # MIDI = MIDI + 2

    elif char == ' ':
        '''Char Espaço Dobra o Volume'''
        varMusica.doubleVolume()

    elif (char =='O' or char == 'o' or char == 'I' or char == 'i' or char == 'U' or char == 'u'):
        '''Aumenta o volume em 10%'''
        varMusica.IncrementVolume()

    elif char == '?' or char == '.': #Aumenta uma oitava/ senão puder aumentar, volta ao caso default
        cont = 0

    elif char == ';':
        varMidi.criaNovoMIDI() #TEM QUE TOCAR General MIDI #76 (Pan Flute) NO CASO DE ';'

    elif char == ',':
        varMidi.criaNovoMIDI() #TEM QUE TOCAR eneral MIDI #20 (Church Organ) NO CASO DE ','

    #La
    elif char == 'A':
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/La.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_La.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)

    #Si
    elif char == 'B':
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Si.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Si.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)

    #Do
    elif char == 'C':
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Do.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Do.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)

    #Re
    elif char == 'D':
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Re.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Re.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)

    #Mi
    elif char == 'E':
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Mi.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Mi.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)

    #Fa
    elif char == 'F':
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Fa.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Fa.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)

    #Sol
    elif char == 'G':
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/Sol.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_Sol.wav')
        varGerMusica.hz_to_MIDI(varMidi, varMusica)

    elif char == 'a' or char == 'b' or char == 'c' or char == 'd' or char == 'e' or char == 'f' or char == 'g':
        '''Se vem esses caracteres toca a nota(.wav) que já esta armazenado na varMusica'''
        if varMusica.getAntigoWav() != "../Pasta_dos_Arquivos/silence.wav" and varMusica.getAntigoWav() != "":
            varGerMusica.hz_to_MIDI(varMidi, varMusica)
        else:
            varMusica.setAntigoWav("../Pasta_dos_Arquivos/silence.wav")
            varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_silence.wav')
            varGerMusica.criaWav('../Pasta_dos_Arquivos/novo_silence.wav', 'novissimo.wav', varMusica)

    elif char == '\n':
        varMidi.criaNovoMIDI(53) #General MIDI #15 (Tubular Bells) => 53

    elif char == '!':
        varMidi.criaNovoMIDI(17) #General MIDI #7 (Harpsichord) => 17

    #Qualquer consoante que não as notas
    elif ord(char) >= 72 or ord(char) <= 90 or ord(char) >= 104 or ord(char) <= 122:
        if varMusica.getAntigoWav() == "../Pasta_dos_Arquivos/silence.wav":
            varGerMusica.criaWav('../Pasta_dos_Arquivos/novo_silence.wav', 'novissimo.wav', varMusica)
        else:
            varGerMusica.hz_to_MIDI(varMidi, varMusica)

    #Silêncio
    else:
        varMusica.setAntigoWav("../Pasta_dos_Arquivos/silence.wav")
        varMusica.setnovoWav('../Pasta_dos_Arquivos/novo_silence.wav')
        varGerMusica.criaWav('../Pasta_dos_Arquivos/novo_silence.wav', 'novissimo.wav', varMusica)

#__main__
def main(args):
    #inicialização de algumas bibliotecas e classes
    app = QApplication(args)
    window = Window()
    sys.exit(app.exec_())

#Inicialização das estruturas varMusica e varMidi.
def InicializaEstruturas(string):
    t = Texto()
    t.geraTXT(string)
    # Colocar todas os caracteres do saida.txt no data
    with open('saida.txt') as f:
        data = f.read()

    varMidi = Midi("output.mid", 0, 0, 0, 100, 1)#name, track, time, channel, volume, duration
    varMidi.setNovo()

    varMusica = Musica(120)
    varMusica.setOitava(12)

    # Mandar cada letra do texto para a função mapeiaCaractere
    for i in data:
        mapeiaCaractere(i, varMidi, varMusica)

    # Cria o MIDI final
    varMidi.setMIDI()

if __name__ == '__main__':
    main(sys.argv)
