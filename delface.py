# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delface.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(586, 479)
        Dialog.setStyleSheet("background:rgb(189, 183, 255)")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 50, 241, 261))
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 211, 201))
        self.listWidget.setObjectName("listWidget")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 50, 221, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 30, 211, 201))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 360, 75, 23))
        self.pushButton.setStyleSheet("background:rgb(138, 170, 155);\n"
"border:1px solid black;\n"
"border-radius:8px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 360, 75, 23))
        self.pushButton_2.setStyleSheet("background:rgb(138, 170, 155);\n"
"border:1px solid black;\n"
"border-radius:8px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 260, 31, 21))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "选择学生班级"))
        self.groupBox_2.setTitle(_translate("Dialog", "选择学生"))
        self.pushButton.setText(_translate("Dialog", "删除"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
        self.pushButton_3.setText(_translate("Dialog", "选中"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
