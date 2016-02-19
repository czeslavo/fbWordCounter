# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri Feb 19 18:08:11 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(450, 582)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 19, 411, 215))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.yourFriendsNameInput = QtGui.QLineEdit(self.gridLayoutWidget)
        self.yourFriendsNameInput.setObjectName(_fromUtf8("yourFriendsNameInput"))
        self.gridLayout.addWidget(self.yourFriendsNameInput, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.wordsInput = QtGui.QPlainTextEdit(self.gridLayoutWidget)
        self.wordsInput.setObjectName(_fromUtf8("wordsInput"))
        self.gridLayout.addWidget(self.wordsInput, 5, 0, 1, 1)
        self.yourNameInput = QtGui.QLineEdit(self.gridLayoutWidget)
        self.yourNameInput.setObjectName(_fromUtf8("yourNameInput"))
        self.gridLayout.addWidget(self.yourNameInput, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 240, 411, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.output = QtGui.QTextBrowser(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(20, 280, 411, 281))
        self.output.setObjectName(_fromUtf8("output"))
        self.statusBar = QtGui.QLabel(self.centralwidget)
        self.statusBar.setGeometry(QtCore.QRect(20, 560, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.statusBar.setFont(font)
        self.statusBar.setText(_fromUtf8(""))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "facebook messages word counter", None))
        self.yourFriendsNameInput.setText(_translate("MainWindow", "Insert your friend\'s name", None))
        self.label.setText(_translate("MainWindow", "Your name", None))
        self.wordsInput.setPlainText(_translate("MainWindow", "Type words (separated by semicolons)", None))
        self.yourNameInput.setText(_translate("MainWindow", "Insert your name", None))
        self.label_2.setText(_translate("MainWindow", "Your friend\'s name", None))
        self.label_3.setText(_translate("MainWindow", "Words to count", None))
        self.pushButton.setText(_translate("MainWindow", "Count", None))

