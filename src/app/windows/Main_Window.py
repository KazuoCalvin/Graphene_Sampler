from PyQt5 import QtWidgets, uic
import sys

from core.settings import store_database_path, load_database_path

class MainWindow(QtWidgets.QMainWindow):


    def __init__(self):
        
        # Initialize the parent class
        super(MainWindow, self).__init__()
        
        # Load the UI
        uic.loadUi("src/app/ui/Main_Window.ui", self)
        self.show()
        
        # load database path from settings
        self.database_path = load_database_path()
        
        if self.database_path:
            self.database_path_disp.setText(self.database_path)
        else:
            self.database_path_disp.setText("No database selected")

        # connect database button
        self.database_browse_button.clicked.connect(self.select_database_path)
        
        
    def select_database_path(self):
        
        dlg = QtWidgets.QFileDialog(self, "Select Database File")
        dlg.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        dlg.setViewMode(QtWidgets.QFileDialog.List)

        if dlg.exec_():
            
            selected_files = dlg.selectedFiles()
            
            if selected_files:

                self.database_path = selected_files[0]
                self.database_path_disp.setText(self.database_path)
                store_database_path(self.database_path)