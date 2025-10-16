from PyQt5 import QtWidgets, uic

class SearchTab:

    def __init__(self, parent: QtWidgets.QWidget):

        self.parent = parent
        uic.loadUi("src/app/ui/Search_Tab.ui", self.parent)