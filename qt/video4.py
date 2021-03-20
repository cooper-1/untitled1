# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video4.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 100, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 100, 500, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(400, 200, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.hide()#开局设置隐藏按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 200, 100, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 150, 100, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 150, 500, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 200, 100, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        self.pushButton.clicked.connect(self.slot1)
        self.pushButton_2.clicked.connect(self.lineEdit_2.clear)
        self.pushButton.clicked.connect(self.pushButton_3.hide)
        self.pushButton_3.clicked.connect(self.pushButton.show)
        self.pushButton.clicked.connect(self.pushButton.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "爬取樱花AV"))
        self.label_2.setText(_translate("MainWindow", "请输入URL ："))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "https://yinghuaav.site/vodtype/27.html"))
        self.pushButton.setText(_translate("MainWindow", "执行"))
        self.pushButton_2.setText(_translate("MainWindow", "重构"))
        self.label_3.setText(_translate("MainWindow", "请输入页数："))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "一页24个视频大约3小时下载一页"))
        self.pushButton_3.setText(_translate("MainWindow", "保存"))

    def slot1(self):
        print('正在执行')
        self.label.setText("正在爬取请稍后。。。。。")
        time.sleep(10)


import sys  #导入系统模块
def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)         #实例化QApplication类，作为GUI主程序入口
    MainWindow=QtWidgets.QMainWindow()             #创建MainWindow
    ui=Ui_MainWindow()                             #实例化ui类
    ui.setupUi(MainWindow)                         #设置窗口UI
    MainWindow.show()                              #显示窗口
    sys.exit(app.exec_())                          #当窗口创建完成时，需要结束主循环过程
if __name__=="__main__":
    show_MainWindow()