import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout
import csv

class InputWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Input Window")
        self.setGeometry(100, 100, 400, 200)
        
        self.id_label = QLabel("DocID:")
        self.id_input = QLineEdit()

        self.name_label = QLabel("DocName:")
        self.name_input = QLineEdit()

        self.gen_label = QLabel("Gender:")
        self.gen_input = QLineEdit()

        self.dept_label = QLabel("Department:")
        self.dept_input = QLineEdit()

        self.sal_label = QLabel("Salary:")
        self.sal_input = QLineEdit()

        self.exp_label = QLabel("Experience:")
        self.exp_input = QLineEdit()

        self.dob_label = QLabel("DOB:")
        self.dob_input = QLineEdit()
        
        self.submit_button = QPushButton("Submit")

        layout = QFormLayout()
        layout.addRow(self.id_label, self.id_input)
        layout.addRow(self.name_label, self.name_input)
        layout.addRow(self.gen_label, self.gen_input)
        layout.addRow(self.dept_label, self.dept_input)
        layout.addRow(self.sal_label, self.sal_input)
        layout.addRow(self.exp_label, self.exp_input)
        layout.addRow(self.dob_label, self.dob_input)
        
        layout.addRow(self.submit_button)

        self.setLayout(layout)

        self.submit_button.clicked.connect(self.save_input_data)

    def save_input_data(self):
        docID = self.id_input.text()
        name = self.name_input.text()
        gen = self.gen_input.text()
        dept = self.dept_input.text()
        sal = self.sal_input.text()
        exp = self.exp_input.text()
        dob = self.dob_input.text()

        with open("data.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([docID, name, gen, dept, sal, exp, dob])

        self.close()  # Close the window after saving the data

def main():
    app1 = QApplication(sys.argv)
    window1 = InputWindow()
    window1.show()
    app1.exec_()

if __name__ == "__main__":
    main()
