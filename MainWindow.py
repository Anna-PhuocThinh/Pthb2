# Form implementation generated from reading ui file 'D:\Tuduylaptrinh\git-demo\Dev_at_Apple\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(90, 70, 461, 271))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 441, 31))
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 441, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEditX1 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditX1.setObjectName("lineEditX1")
        self.gridLayout.addWidget(self.lineEditX1, 3, 1, 1, 1)
        self.lineEditB = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditB.setObjectName("lineEditB")
        self.gridLayout.addWidget(self.lineEditB, 1, 1, 1, 1)
        self.lineEditC = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditC.setObjectName("lineEditC")
        self.gridLayout.addWidget(self.lineEditC, 2, 1, 1, 1)
        self.lineEditA = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditA.setObjectName("lineEditA")
        self.gridLayout.addWidget(self.lineEditA, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.lineEditX2 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditX2.setObjectName("lineEditX2")
        self.gridLayout.addWidget(self.lineEditX2, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(170, 230, 111, 21))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#000000;\">PHƯƠNG TRÌNH BẬC 2</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Giá trị X1"))
        self.label_2.setText(_translate("MainWindow", "Nhập A"))
        self.label_4.setText(_translate("MainWindow", "Nhập C"))
        self.label_3.setText(_translate("MainWindow", "Nhập B"))
        self.label_6.setText(_translate("MainWindow", "Giá trị X2"))
        self.pushButton.setText(_translate("MainWindow", "THỰC HIỆN"))