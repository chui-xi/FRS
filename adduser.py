# -*- coding: utf-8 -*-123

# Form implementation generated from reading ui file 'adduser.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(967, 597)
        Dialog.setStyleSheet("background:rgb(189, 183, 255)")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 401, 271))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 330, 111, 41))
        self.pushButton.setStyleSheet("border:1px solid black;\n"
"border-radius:8px")
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(770, 40, 191, 221))
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 171, 191))
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 480, 171, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 490, 36, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 410, 131, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 550, 31, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 540, 171, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(870, 510, 75, 23))
        self.pushButton_2.setStyleSheet("background:rgb(138, 170, 155);\n"
"border:1px solid black;\n"
"border-radius:8px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(870, 560, 75, 23))
        self.pushButton_3.setStyleSheet("background:rgb(138, 170, 155);\n"
"border:1px solid black;\n"
"border-radius:8px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 540, 91, 41))
        self.pushButton_4.setStyleSheet("border:1px solid black;\n"
"border-radius:8px")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(450, 20, 311, 291))
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(550, 330, 101, 41))
        self.pushButton_5.setStyleSheet("border:1px solid black;\n"
"border-radius:8px")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 330, 111, 41))
        self.pushButton_6.setStyleSheet("border:1px solid black;\n"
"border-radius:8px")
        self.pushButton_6.setObjectName("pushButton_6")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 10, 431, 311))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(440, 10, 321, 311))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(53, 411, 171, 41))
        self.comboBox.setStyleSheet("font: 60pt \"ADMUI3Lg\";")
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 420, 36, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "选择人脸图片"))
        self.groupBox.setTitle(_translate("Dialog", "选择班级添加学生"))
        self.label_2.setText(_translate("Dialog", "学号："))
        self.label_4.setText(_translate("Dialog", "部门："))
        self.pushButton_2.setText(_translate("Dialog", "确定"))
        self.pushButton_3.setText(_translate("Dialog", "取消"))
        self.pushButton_4.setText(_translate("Dialog", "导入数据"))
        self.label_5.setText(_translate("Dialog", "                         添加照片"))
        self.pushButton_5.setText(_translate("Dialog", "添加人脸照片"))
        self.pushButton_6.setText(_translate("Dialog", "打开摄像头"))
        self.label_3.setText(_translate("Dialog", "姓名："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
