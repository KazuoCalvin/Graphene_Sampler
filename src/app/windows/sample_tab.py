from PyQt5 import QtWidgets, uic

class SampleTab:

    def __init__(self, parent: QtWidgets.QWidget):

        self.parent = parent
        uic.loadUi("src/app/ui/Sample_Tab.ui", self.parent)