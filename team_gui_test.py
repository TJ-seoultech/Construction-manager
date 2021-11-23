from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from team_if_work import work_instruction


ui_file = "./gui_section1_test.ui"


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file,self)

        self.work_process = ["1.토공사", "2.기초공사", "3.골조공사", "4.조적공사", "5.미장공사", "6.방수공사", "7.지붕공사", "8.창호공사", "9.도장공사"]
        self.work_selection = []
        self.message_printed = []

        self.pushButton.clicked.connect(lambda state, button = self.pushButton : self.buttonclick(state, button))
        self.pushButton_2.clicked.connect(lambda state, button = self.pushButton_2 : self.buttonclick(state, button))
        self.pushButton_3.clicked.connect(lambda state, button = self.pushButton_3 : self.buttonclick(state, button))
        self.pushButton_4.clicked.connect(lambda state, button = self.pushButton_4 : self.buttonclick(state, button))
        self.pushButton_5.clicked.connect(lambda state, button = self.pushButton_5 : self.buttonclick(state, button))
        self.pushButton_6.clicked.connect(lambda state, button = self.pushButton_6 : self.buttonclick(state, button))
        self.pushButton_7.clicked.connect(lambda state, button = self.pushButton_7 : self.buttonclick(state, button))
        self.pushButton_8.clicked.connect(lambda state, button = self.pushButton_8 : self.buttonclick(state, button))
        self.pushButton_9.clicked.connect(lambda state, button = self.pushButton_9 : self.buttonclick(state, button))

    def buttonclick(self, state, button):
        clicked_work = button.text()
        for work_num in range(len(self.work_process)):
            if self.work_process[work_num] == clicked_work:
                self.work_selection.append(work_num)
                self.work_note(work_num)
            else: pass


    def work_note(self, num):
        self.print_text(work_instruction(num))

    def print_text(self, text):
        self.message_1.append(text)

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())
# app.exec_()