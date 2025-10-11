from PyQt5.QtWidgets import QApplication
from windows.Main_Window import MainWindow
import sys

def main():
    app = QApplication(sys.argv)
    MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()