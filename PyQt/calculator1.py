# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 651)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(150, 40, 501, 101))
        self.lcdNumber.setObjectName("lcdNumber")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(140, 170, 541, 411))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.button_bksp = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_bksp.sizePolicy().hasHeightForWidth())
        self.button_bksp.setSizePolicy(sizePolicy)
        self.button_bksp.setObjectName("button_bksp")
        self.gridLayout.addWidget(self.button_bksp, 0, 2, 1, 1)
        self.button_C = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_C.sizePolicy().hasHeightForWidth())
        self.button_C.setSizePolicy(sizePolicy)
        self.button_C.setObjectName("button_C")
        self.gridLayout.addWidget(self.button_C, 0, 3, 1, 1)
        self.button_7 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)
        self.button_7.setObjectName("button_7")
        self.gridLayout.addWidget(self.button_7, 1, 0, 1, 1)
        self.button_8 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)
        self.button_8.setObjectName("button_8")
        self.gridLayout.addWidget(self.button_8, 1, 1, 1, 1)
        self.button_9 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)
        self.button_9.setObjectName("button_9")
        self.gridLayout.addWidget(self.button_9, 1, 2, 1, 1)
        self.button_plus = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_plus.sizePolicy().hasHeightForWidth())
        self.button_plus.setSizePolicy(sizePolicy)
        self.button_plus.setObjectName("button_plus")
        self.gridLayout.addWidget(self.button_plus, 1, 3, 1, 1)
        self.button_4 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        self.button_4.setObjectName("button_4")
        self.gridLayout.addWidget(self.button_4, 2, 0, 1, 1)
        self.button_5 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        self.button_5.setObjectName("button_5")
        self.gridLayout.addWidget(self.button_5, 2, 1, 1, 1)
        self.button_6 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)
        self.button_6.setObjectName("button_6")
        self.gridLayout.addWidget(self.button_6, 2, 2, 1, 1)
        self.button_minus = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_minus.sizePolicy().hasHeightForWidth())
        self.button_minus.setSizePolicy(sizePolicy)
        self.button_minus.setObjectName("button_minus")
        self.gridLayout.addWidget(self.button_minus, 2, 3, 1, 1)
        self.button_1 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)
        self.button_1.setObjectName("button_1")
        self.gridLayout.addWidget(self.button_1, 3, 0, 1, 1)
        self.button_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)
        self.button_2.setObjectName("button_2")
        self.gridLayout.addWidget(self.button_2, 3, 1, 1, 1)
        self.button_3 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)
        self.button_3.setObjectName("button_3")
        self.gridLayout.addWidget(self.button_3, 3, 2, 1, 1)
        self.button_multi = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_multi.sizePolicy().hasHeightForWidth())
        self.button_multi.setSizePolicy(sizePolicy)
        self.button_multi.setObjectName("button_multi")
        self.gridLayout.addWidget(self.button_multi, 3, 3, 1, 1)
        self.button_comma = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_comma.sizePolicy().hasHeightForWidth())
        self.button_comma.setSizePolicy(sizePolicy)
        self.button_comma.setObjectName("button_comma")
        self.gridLayout.addWidget(self.button_comma, 4, 0, 1, 1)
        self.button_0 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy)
        self.button_0.setObjectName("button_0")
        self.gridLayout.addWidget(self.button_0, 4, 1, 1, 1)
        self.button_equal = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_equal.sizePolicy().hasHeightForWidth())
        self.button_equal.setSizePolicy(sizePolicy)
        self.button_equal.setObjectName("button_equal")
        self.gridLayout.addWidget(self.button_equal, 4, 2, 1, 1)
        self.button_division = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_division.sizePolicy().hasHeightForWidth())
        self.button_division.setSizePolicy(sizePolicy)
        self.button_division.setObjectName("button_division")
        self.gridLayout.addWidget(self.button_division, 4, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_bksp.setText(_translate("Form", "⬅"))
        self.button_C.setText(_translate("Form", "C"))
        self.button_7.setText(_translate("Form", "7"))
        self.button_8.setText(_translate("Form", "8"))
        self.button_9.setText(_translate("Form", "9"))
        self.button_plus.setText(_translate("Form", "+"))
        self.button_4.setText(_translate("Form", "4"))
        self.button_5.setText(_translate("Form", "5"))
        self.button_6.setText(_translate("Form", "6"))
        self.button_minus.setText(_translate("Form", "-"))
        self.button_1.setText(_translate("Form", "1"))
        self.button_2.setText(_translate("Form", "2"))
        self.button_3.setText(_translate("Form", "3"))
        self.button_multi.setText(_translate("Form", "*"))
        self.button_comma.setText(_translate("Form", "."))
        self.button_0.setText(_translate("Form", "0"))
        self.button_equal.setText(_translate("Form", "="))
        self.button_division.setText(_translate("Form", "/"))
