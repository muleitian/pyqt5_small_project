# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(877, 665)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(130, 80, 481, 381))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 50, 72, 15))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(50, 110, 371, 211))
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(180, 50, 181, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.queryBtn = QtWidgets.QPushButton(Form)
        self.queryBtn.setGeometry(QtCore.QRect(170, 520, 93, 28))
        self.queryBtn.setObjectName("queryBtn")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(480, 520, 93, 28))
        self.clearBtn.setObjectName("clearBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "查询城市天气"))
        self.label.setText(_translate("Form", "城市"))
        self.comboBox.setItemText(0, _translate("Form", "北京"))
        self.comboBox.setItemText(1, _translate("Form", "天津"))
        self.comboBox.setItemText(2, _translate("Form", "上海"))
        self.comboBox.setItemText(3, _translate("Form", "西安"))
        self.queryBtn.setText(_translate("Form", "查询"))
        self.clearBtn.setText(_translate("Form", "清空"))
