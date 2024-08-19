import asyncio
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QDialog, QMessageBox
import errorcodes
from app import Ui_MainWindow
from PySide6.QtGui import QGuiApplication
from PySide6 import QtCore
import sys
from ressources import ressources
from asyncio import *




class Operation:
    def __init__(self):
        pass


#Main App

class app_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)









App = QApplication(sys.argv)
window = app_window()
window.show()

App.exec()



