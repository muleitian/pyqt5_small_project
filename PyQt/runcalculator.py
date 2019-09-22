import sys
from PyQt5 import QtGui,QtWidgets,uic
from PyQt5.QtWidgets import QMainWindow
from calculator1 import Ui_Form
class MyForm(QMainWindow):
    firstvalue=0
    secondvalue=0
    action=''
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.button_1.clicked.connect(self.buttonClicked)
        self.ui.button_2.clicked.connect(self.buttonClicked)
        self.ui.button_3.clicked.connect(self.buttonClicked)
        self.ui.button_4.clicked.connect(self.buttonClicked)
        self.ui.button_5.clicked.connect(self.buttonClicked)
        self.ui.button_6.clicked.connect(self.buttonClicked)
        self.ui.button_7.clicked.connect(self.buttonClicked)
        self.ui.button_8.clicked.connect(self.buttonClicked)
        self.ui.button_9.clicked.connect(self.buttonClicked)
        self.ui.button_0.clicked.connect(self.buttonClicked)

        self.ui.button_plus.clicked.connect(self.action_button)
        self.ui.button_minus.clicked.connect(self.action_button)
        self.ui.button_multi.clicked.connect(self.action_button)
        self.ui.button_division.clicked.connect(self.action_button)
        self.ui.button_equal.clicked.connect(self.result)
        self.ui.button_C.clicked.connect(self.clean)
        self.ui.button_comma.clicked.connect(self.buttonClicked)
        self.ui.button_bksp.clicked.connect(self.backspace)
    def buttonClicked(self):
        if self.ui.button_equal.isEnabled()==False:
            self.ui.lcdNumber.display(0)
            self.ui.button_equal.setEnabled(True)
        sender=self.sender()
        x=str(self.ui.lcdNumber.value())
        if self.ui.button_comma.isEnabled()==True:
            x=x[:-2]
            if sender.text()=='.':
                x+=sender.text()
                self.ui.button_comma.setEnabled(False)
            else :
                if x=='0':
                    x=sender.text()
                else :
                    x+=sender.text()
        else :
            if self.ui.button_comma.isChecked()==True:
                self.ui.button_comma.setCheckable(False)
                x=x[:-1]+sender.text()
            else :
                x+=sender.text()
        if len(x)>7:
            self.ui.lcdNumber.setDigitCount(len(x))
        self.ui.lcdNumber.display(x)
    def action_button(self):
        global firstvalue,action
        sender=self.sender()
        firstvalue=self.ui.lcdNumber.value()
        self.ui.lcdNumber.display(0)
        action=sender.text()
        self.ui.button_comma.setEnabled(True)
        self.ui.button_comma.setCheckable(True)
        self.ui.lcdNumber.setDigitCount(7)
    def result(self):
        global firstvalue,secondvalue,action
        secondvalue=self.ui.lcdNumber.value()
        if action=="+":
            x=firstvalue+secondvalue
        elif action=="-":
            x=firstvalue-secondvalue
        elif action=="*":
            x=firstvalue-secondvalue
        elif action=="/":
            x=firstvalue/secondvalue
        x=str(x)
        if len(x)-x.index(".")>3:
            y=len(x)-x.index(".") -3
            x=x[:-y]
        if x.endswith(".0"):
            x=x[:-2]
        if len(x)>7:
            self.ui.lcdNumber.setDigitCount(len(x))
        self.ui.lcdNumber.display(x)
        firstvalue=0
        secondvalue=0
        action=""
        self.ui.button_comma.setCheckable(True)
        self.ui.button_comma.setEnabled(True)
        self.ui.button_equal.setEnabled(False)


    def clean(self):
        global firstvalue,secondvalue,action
        self.ui.lcdNumber.display(0)
        firstvalue=0
        secondvalue=0
        action=''
        self.ui.button_comma.setEnabled(True)
        self.ui.button_comma.setCheckable(True)
        self.ui.lcdNumber.setDigitCount(7)
    def backspace(self):
        x=str(self.ui.lcdNumber.value())
        if self.ui.button_comma.isEnabled()==True:
            x=x[:-3]
        else :
            x=x[:-1]
        if len(x)>7:
            self.ui.lcdNumber.setDigitCount(len(x))
        else :
            self.ui.lcdNumber.setDigitCount(7)
        self.ui.lcdNumber.display(x)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())









