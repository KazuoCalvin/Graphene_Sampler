from PyQt5 import QtWidgets, uic
import sys

class MainWindow(QtWidgets.QMainWindow):

    
    def __init__(self):
        
        # Initialize the parent class
        super(MainWindow, self).__init__()
        
        # Load the UI
        uic.loadUi("src/app/ui/Main_Window.ui", self)  # Load the .ui file
        self.show()
        
        # connect database button
        self.database_browse_button.clicked.connect(self.select_database_path)
        
        
    def select_database_path(self):
        
        dlg = QtWidgets.QFileDialog(self, "Select Database File")
        dlg.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        dlg.setViewMode(QtWidgets.QFileDialog.List)

        if dlg.exec_():
            
            selected_files = dlg.selectedFiles()
            
            if selected_files:
                database_path = selected_files[0]
                self.database_path.setText(database_path)