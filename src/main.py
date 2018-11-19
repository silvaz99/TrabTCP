# Trabalho TCP 2018/2
from classes import *
from TKinterface import *


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


def main():
    root = tkinter.Tk()
    # root2 = tkinter.Tk()
    root.geometry("800x480")
    # app = Window(root)
    # menubar = Menu(root)

    t = Texto("ABCDEFG")
    t.geraTXT()

    # Colocar todas os caracteres do saida.txt no data
    with open('saida.txt') as f:
        data = f.read()

    # layout all of the main containers
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    # root2.grid_rowconfigure(1, weight=1)
    # root2.grid_columnconfigure(1, weight=1)


    f1 = Frame(root, height = 120, width = 120)
    f1.grid(row = 2, column = 1)
    f2 = Frame(root, height = 120, width = 120)
    f2.grid(row = 2, column = 2)

    loadimage = PhotoImage(file = "dest.png")
    PlayButton = Button(f1, image = loadimage, command = lambda:mapeia1(data))
    PlayButton["bg"] = "white"
    PlayButton["border"] = "0"
    # PlayButton.grid(row=2, column=3, columnspan=2)
    PlayButton.pack(side="top", fill=BOTH)

    loadimage2 = PhotoImage(file = "stop2.png")
    StopButton = Button(f2, image = loadimage2, command = lambda:exit())
    StopButton["bg"] = "white"
    StopButton["border"] = "0"
    # StopButton.grid(row=2, column=3, columnspan=2)
    StopButton.pack(side="top", fill=BOTH)

    # b = Button(f, text="OK", command = lambda:mapeia1(data))
    # b.pack(fill=BOTH, expand=1)
    root.mainloop()


def mapeia1(data):
    varMidi = Midi("output.mid", 0, 0, 0, 100, 1)          #name, track, time, channel, volume, duration
    varMusica = Musica(120)
    varMusica.setOitava(12)
    # Mandar cada letra do texto para a função Mapeia
    for i in data:
        mapeia(i, varMidi, varMusica)



if __name__ == '__main__':
    main()
