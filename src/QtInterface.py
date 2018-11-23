import sys
from random import randint
from main import *

# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QPlainTextEdit, QMainWindow, QTextEdit,QMenuBar, QAction, QToolBar, QMessageBox, qApp
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.initUi()

        self.low = 10
        self.high = 100

        self.show()


    def initUi(self):

        self.button = QPushButton(' Play ')
        self.buttonPause = QPushButton(' Quit ')
        self.text_edit = QPlainTextEdit()

        self.MenuBar = QMenuBar()
        Menu = self.MenuBar.addMenu('File')

        Exit = self.MenuBar.addAction('', self.exit)
        Exit.setIcon(QtGui.QIcon('exit.png'))

        


        self.label = QLabel()


        self.layout = QGridLayout()
        # self.layout.columnMinimumWidth(10)
        self.layout.setSpacing(100)
        self.layout.addWidget(self.MenuBar, 0, 0)
        self.layout.addWidget(self.button, 5, 0)
        self.layout.addWidget(self.text_edit, 1, 0)
        # self.layout.addWidget(self.label, 0, 0)

        text = self.text_edit.textChanged.connect(lambda: self.carregaTexto(self.text_edit, self.label))
        # print(text)
        self.button.clicked.connect(lambda: self.carregaTexto(text, self.label))
        self.button.setIcon(QtGui.QIcon('dest.png'))
        self.button.setIconSize(QtCore.QSize(36,24))

        self.buttonPause.clicked.connect(self.exit)
        self.buttonPause.setIcon(QtGui.QIcon('stop2.png'))
        self.buttonPause.setIconSize(QtCore.QSize(36,24))


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

    def on_button_clicked(self):

        value = str(randint(self.low, self.high))
        self.label.setText(value)

    def carregaTexto(self, text_edit, label):
        text = text_edit.toPlainText()
        self.button.clicked.connect(lambda : mapeia1(text))

        if '\n' in text:
            text = list(text)
            text[-1] = ''
            text = ''.join(text)
            return mapeia1(text)

    def exit(self):
        exit()
