from PyQt5 import QtWidgets, uic
import sys

class MainWindow(QtWidgets.QMainWindow):

    
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("src/app/ui/Main_Window.ui", self)  # Load the .ui file
        self.show()