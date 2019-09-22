from PyQt5.QtWidgets import *
import  sys
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
'''
class QlineEditchoMode(QWidget):
    def __init__(self):
        super(QlineEditchoMode,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')
        formlayout=QFormLayout()
        normallineEdit=QLineEdit()
        noEchoLineEdit=QLineEdit()
        passordLineEdit=QLineEdit()
        passwordEchonEditLineEdit=QLineEdit()

        formlayout.addRow('normal',normallineEdit)
        formlayout.addRow('notecho',normallineEdit)
        formlayout.addRow('password',passordLineEdit)
        formlayout.addRow('passwordEchoOnEdit',passwordEchonEditLineEdit)

        normallineEdit.setPlaceholderText('normal')
        noEchoLineEdit.setPlaceholderText('Npecho')
        passordLineEdit.setPlaceholderText('passord')
        passwordEchonEditLineEdit.setPlaceholderText('passwordEchoOnEdit')

        normallineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchonEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formlayout)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QlineEditchoMode()
    main.show()
    sys.exit(app.exec_())
'''
'''
class QLineEditVakidator(QWidget):
    def __init__(self):
        super(QLineEditVakidator,self).__init__()
        self.initUI()
    def initUI(self):
       self.setWindowTitle('校验器')
       formlayout=QFormLayout()
       initLineEdit=QLineEdit()
       doubleEdit=QLineEdit()
       validatorLineEdit=QLineEdit()

       formlayout.addRow('整数类型',initLineEdit)
       formlayout.addRow('浮点数类型',doubleEdit)
       formlayout.addRow('数字和浮点数',validatorLineEdit)

       initLineEdit.setPlaceholderText('整型')
       doubleEdit.setPlaceholderText('浮点数')
       validatorLineEdit.setPlaceholderText('字母和数字')

       initValidator=QIntValidator(self)
       initValidator.setRange(1,99)

       doubleValidator=QDoubleValidator(self)
       doubleValidator.setRange(-360,360)
       doubleValidator.setNotation(QDoubleValidator.StandardNotation)
       doubleValidator.setDecimals(2)

       reg=QRegExp('[a-zA-Z0-9]+$')
       validator=QRegExpValidator(self)
       validator.setRegExp(reg)

       initLineEdit.setValidator(initValidator)
       doubleEdit.setValidator(doubleValidator)
       validatorLineEdit.setValidator(validator)

       self.setLayout(formlayout)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLineEditVakidator()
    main.show()
    sys.exit(app.exec_())
'''
'''
class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.initUI()
    def textChanged(self,text):
            print('输入内容'+text)
    def enterprass(self):
        print('已输入值')
    def initUI(self):
        edit1=QLineEdit()
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial',20))
        edit2=QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99,9.99,2))
        edit3=QLineEdit()
        edit3.setInputMask('99_9999_9999999;#')
        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChanged)
        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterprass)
        edit6 = QLineEdit('hello pyqt5')
        edit6.setReadOnly(True)



        formlayout=QFormLayout()
        formlayout.addRow('整数校验器',edit1)
        formlayout.addRow('浮点数校验',edit2)
        formlayout.addRow('inputmask',edit3)
        formlayout.addRow('文本变化',edit4)
        formlayout.addRow('密码',edit5)
        formlayout.addRow('只读',edit6)

        edit2.setAlignment(Qt.AlignRight)
        edit2.setFont(QFont('Arial', 20))
        edit3.setFont(QFont('Arial', 10))






        self.setLayout(formlayout)
        self.setWindowTitle('QLineEdit综合案例')

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLineEditDemo()
    main.show()
    sys.exit(app.exec_())
'''
'''
class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()
    def onClick_ButtonText(self):
        self.textEdit.setPlainText('hello word,世界你好吗？')
    def onClick_ButtonToText(self):
        print(self.textEdit.toPlainText())
    def onclick_ButtonToHtml(self):
        print(self.textEdit.toHtml())
    def onclick_ButtonHtml(self):
        self.textEdit.setHtml('<font color="red" size="5"> hello world</font>')

    def initUI(self):
        self.setWindowTitle('QTexEdit控件演示')
        self.resize(300,280)
        self.textEdit=QTextEdit()
        self.buttonText=QPushButton('显示文本')
        self.buttonHtml=QPushButton('显示Html')
        self.buttonToText = QPushButton('获取文本')
        self.buttonToHtml = QPushButton('获取Html')

        layout=QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHtml)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonToHtml)
        self.setLayout(layout)
        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHtml.clicked.connect(self.onclick_ButtonHtml)
        self.buttonToText.clicked.connect(self.onClick_ButtonToText)
        self.buttonToHtml.clicked.connect(self.onclick_ButtonToHtml)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QTextEditDemo()
    main.show()
    sys.exit(app.exec_())
'''
'''
class QRadiobutton(QDialog):
    def __init__(self):
        super(QRadiobutton, self).__init__()
        self.initUI()
    def buttonState(self):
        radioButton=self.sender()
        if radioButton.text()=='单选按钮1':
            if radioButton.isChecked==True:
                print('<'+radioButton.text()+'>被选中')
            else:print('<'+radioButton.text()+'>取消被选中状态')
    def initUI(self):
        self.setWindowTitle('QRadiobutton Demo')
        layout=QHBoxLayout()
        self.button1=QRadioButton('单选按钮1')
        self.button2 = QRadioButton('单选按钮2')
        self.button1.setChecked(True)
        self.button1.toggled.connect(self.buttonState)
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QRadiobutton()
    main.show()
    sys.exit(app.exec_())
'''
'''
class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('复选框控件演示')
        layout=QHBoxLayout()
        self.checkBox1=QCheckBox('复选框控件1')
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda :self.checkboxState(self.checkBox1))
        layout.addWidget(self.checkBox1)
        self.checkBox2 = QCheckBox('复选框控件2')
        self.checkBox2.stateChanged.connect(lambda: self.checkboxState(self.checkBox2))
        layout.addWidget(self.checkBox2)
        self.checkBox3 = QCheckBox('半选中')
        self.checkBox3.stateChanged.connect(lambda: self.checkboxState(self.checkBox3))
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        layout.addWidget(self.checkBox3)

        self.setLayout(layout)


    def checkboxState(self,cb):
        check1State=self.checkBox1.text()+',isChecked='+str(self.checkBox1.isChecked())+',checkState='+str(self.checkBox1.checkState())+'\n'
        check2State= self.checkBox2.text() + ',isChecked=' + str(self.checkBox2.isChecked()) + ',checkState=' + str(self.checkBox2.checkState())+ '\n'
        check3State= self.checkBox3.text() + ',isChecked=' + str(self.checkBox3.isChecked()) + ',checkState=' + str(self.checkBox3.checkState() )+ '\n'
        print(check1State+check2State+check3State)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())
'''
'''
class DrawText(QWidget):
    def __init__(self):
        super(DrawText, self).__init__()
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(300,200)
        self.text='无聊死了'
    def paintEvent(self, event):
        painter=QPainter(self)
        painter.begin(self)
        painter.setPen(QColor(150,43,5))
        painter.setFont(QFont('SimSun',25))
        painter.drawText(event.rect(),Qt.AlignCenter,self.text)


        painter.end(self)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DrawText()
    main.show()
    sys.exit(app.exec_())
'''

































