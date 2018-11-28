#TAD responsável pelo controle e manutenção da interface


#importação de algumas bibliotecas para o funcionamento do programa
import sys
from random import randint
from main import *

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QPlainTextEdit, QMainWindow, QTextEdit,QMenuBar, QAction, QToolBar, QMessageBox, qApp, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets


#Classe responsável pelo gerenciamento da interface
class InterfaceWindow(QWidget):

    #Contrututor da interface
    def __init__(self):

        super().__init__()
        self.iniciaUi()

        self.low = 10
        self.high = 100

        self.show()

    #Contrututor de partes da interface, como botões e barra de menu
    def iniciaUi(self):
        #botão de play
        self.button = QPushButton(' Play ')
        self.text_edit = QPlainTextEdit()

        #barra de menu
        self.MenuBar = QMenuBar()
        Menu = self.MenuBar.addMenu('File')

        #botão de saída
        Exit = self.MenuBar.addAction('', self.exit)
        Exit.setIcon(QtGui.QIcon('exit.png'))

        Menu.addAction('Open File', self.openfiles)

        #configuração de design da interface, como tamanho, posição etc.
        self.label = QLabel()

        self.layout = QGridLayout()
        # self.layout.columnMinimumWidth(10)
        self.layout.setSpacing(100)
        self.layout.addWidget(self.MenuBar, 0, 0)
        self.layout.addWidget(self.button, 5, 0)
        self.layout.addWidget(self.text_edit, 1, 0)
        # self.layout.addWidget(self.label, 0, 0)

        # self.text_edit.textChanged.connect(lambda: self.carregaTexto(self.text_edit, self.label))
        # print(text)
        self.button.clicked.connect(lambda: self.carregaTexto(self.text_edit.toPlainText(), self.label))
        self.button.setIcon(QtGui.QIcon('dest.png'))
        self.button.setIconSize(QtCore.QSize(36,24))

        # self.buttonPause.clicked.connect(self.exit)
        # self.buttonPause.setIcon(QtGui.QIcon('stop2.png'))
        # self.buttonPause.setIconSize(QtCore.QSize(36,24))


        #configuração de design da interface, como tamanho, posição etc.
        self.setLayout(self.layout)
        self.setGeometry(500, 100, 500, 500)

    # def create_actions(self):
    #     self.exit_action = QAction()
    #     self.exit_action.setText('Exit')
    #     self.exit_action.setIcon(QtGui.QIcon('exit.png'))
    #
    #     self.about_action = QAction()
    #     self.about_action.setText('About')
    #     self.about_action.setIcon(QtGui.QIcon('about.png'))
    #
    # def create_menus(self):
    #     menu_bar = self.menuBar()
    #     file_menu = menu_bar.addMenu('File')
    #
    #     file_menu.addAction(self.exit_action)
    #     self.exit_action.triggered.connect(qApp.quit)
    #     help_menu = menu_bar.addMenu('Help')
    #
    #     self.about_action.triggered.connect(self.exit)
    #     help_menu.addAction(self.about_action)


    #método que realiza a ação do botão
    def on_button_clicked(self):
        value = str(randint(self.low, self.high))
        self.label.setText(value)

    #método que carrega o texto digitado na interface e passa para o método que trata da string
    def carregaTexto(self, text, label):
        preMapeamento(text)

        # if '\n' in text:
        #     text = list(text)
        #     text[-1] = ''
        #     text = ''.join(text)
        #     preMapeamento(text)

    #método que lê o que foi salvo em uma variável que contia o conteúdo digitado na interface e passa para o método de tratamento da string
    def openfiles(self):
        filename = QFileDialog.getOpenFileName(None, 'Pasta', os.getcwd(), 'All Files(*.*)')
        #print(type(filename))
        arquivo = open(filename[0], 'r')
        preMapeamento(arquivo.read())

    #método de saída do programa
    def exit(self):
        exit()
