# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(819, 929)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 190, 501, 351))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout.addWidget(self.comboBox_5, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(670, 210, 81, 46))
        self.pushButton.setObjectName("pushButton")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(330, 50, 141, 41))
        self.title.setObjectName("title")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(160, 600, 501, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(170, 560, 108, 24))
        self.label_7.setObjectName("label_7")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(460, 120, 231, 28))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 810, 150, 46))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "SGD"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "RMSprop"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "Adagrad"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "Adadelta"))
        self.comboBox_4.setItemText(4, _translate("Dialog", "Adam"))
        self.comboBox_4.setItemText(5, _translate("Dialog", "Adamax"))
        self.comboBox_4.setItemText(6, _translate("Dialog", "Nadam"))
        self.label_6.setText(_translate("Dialog", "损失函数"))
        self.label_4.setText(_translate("Dialog", "选择数据文件"))
        self.label_5.setText(_translate("Dialog", "优化器"))
        self.label.setText(_translate("Dialog", "模型名称"))
        self.lineEdit.setText(_translate("Dialog", "MyModel"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "mean_squared_error"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "mean_absolute_error"))
        self.comboBox_5.setItemText(2, _translate("Dialog", "mean_absolute_percentage_error"))
        self.comboBox_5.setItemText(3, _translate("Dialog", "mean_squared_logarithmic_error"))
        self.comboBox_5.setItemText(4, _translate("Dialog", "squared_hinge"))
        self.comboBox_5.setItemText(5, _translate("Dialog", "hinge"))
        self.comboBox_5.setItemText(6, _translate("Dialog", "categorical_hinge"))
        self.comboBox_5.setItemText(7, _translate("Dialog", "logcosh"))
        self.label_3.setText(_translate("Dialog", "训练次数"))
        self.comboBox.setItemText(0, _translate("Dialog", "5000"))
        self.comboBox.setItemText(1, _translate("Dialog", "10000"))
        self.comboBox.setItemText(2, _translate("Dialog", "20000"))
        self.comboBox.setItemText(3, _translate("Dialog", "50000"))
        self.pushButton.setText(_translate("Dialog", "检测"))
        self.title.setText(_translate("Dialog", "LSTM模型"))
        self.label_7.setText(_translate("Dialog", "程序输出"))
        self.checkBox.setText(_translate("Dialog", "训练新的模型"))
        self.pushButton_2.setText(_translate("Dialog", "开始训练"))
