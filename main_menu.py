"""
Main Execution File
Modules Used throughout-
1. mysql-connector-python
2. sys
3. PyQT5
4. Tkinter
5. CSV
"""

import sys
import mgmt as mg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QMessageBox
import result_win as rw
import csv

import mysql.connector as rt
cn = rt.connect(host="localhost", user="root", passwd="9889", database="hospital", charset="utf8")
cr = cn.cursor()

class OptionPrompt(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Clinic')
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout()

        self.input_win = None
        # Create buttons for each option
        options = {1:'Display', 2:'Search Record', 3:'Add Record', 4:'Delete Record', 5:'Modify Record', 6:'Graph'}
        for op,option in options.items():
            button = QPushButton(option)
            button.clicked.connect(lambda _, opt=op: self.perform_task(opt))
            layout.addWidget(button)

        # Set the layout for the central widget
        central_widget.setLayout(layout)



    def perform_task(self, opt):
        # Perform the task based on the selected option
        #QMessageBox.information(self, 'Task Result', f'Task for {option} has been performed.')
        if opt == 1:
            r = mg.disp()
            rw.text_win(r)

        elif opt == 2:
            from search_record import Search
            self.search = Search()
            self.search.exec_()

        elif opt == 3:
            from input_window import InputWindow
            if not self.input_win:
                self.input_win = InputWindow()
            self.input_win.exec_()
            mg.addRecord()

        elif opt == 4:
            from delete_data import DeleteR
            self.delete = DeleteR()
            self.delete.exec_()

        elif opt == 5:
            from update_record import UpdateWindow
            self.updateWin = UpdateWindow()
            self.updateWin.exec_()
            mg.updateRecord()

        elif opt == 6:
            mg.graph()


def main():
    app = QApplication(sys.argv)
    window = OptionPrompt()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
