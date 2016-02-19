#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

from mainWindow_ui import Ui_MainWindow
from core import FbWordCounter

class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()

    def __init__(self, counter):
    	super(Worker, self).__init__()
    	self.counter = counter

    @QtCore.pyqtSlot()
    def parse(self):
    	self.counter.parse()
        self.finished.emit()

    @QtCore.pyqtSlot()
    def count(self):
    	self.counter.countWords()
    	self.finished.emit()


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()

        # init fbWordCounter
        self.counter = FbWordCounter("messages.htm")

        self.ui.setupUi(self)

        # thread for parsing
        self.parseThread = QtCore.QThread()
    	self.obj = Worker(self.counter)
    	self.obj.moveToThread(self.parseThread)
    	self.obj.finished.connect(self.parseThread.quit)
    	self.parseThread.started.connect(self.obj.parse)
    	#self.parseThread.finished.connect(self.onParsingEnd)
    	self.startParsing()

    	# thread for counting
    	self.obj2 = Worker(self.counter)
    	self.countThread = QtCore.QThread()
    	self.obj2.moveToThread(self.countThread)
    	self.obj2.finished.connect(self.countThread.quit)
    	self.countThread.started.connect(self.obj2.count)
    	#self.countThread.finished.connect(self.onCountingEnd)

        # slots
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"), self.startCounting)
        QtCore.QObject.connect(self.countThread, QtCore.SIGNAL("finished()"), self.onCountingEnd)
        QtCore.QObject.connect(self.parseThread, QtCore.SIGNAL("finished()"), self.onParsingEnd)

        QtCore.QObject.connect(self.ui.yourFriendsNameInput,QtCore.SIGNAL("editingFinished()"), self.refreshCounterNames)
        QtCore.QObject.connect(self.ui.yourNameInput,QtCore.SIGNAL("editingFinished()"), self.refreshCounterNames)
        QtCore.QObject.connect(self.ui.wordsInput,QtCore.SIGNAL("textChanged()"), self.refreshCounterWords)

    def startParsing(self):
    	self.ui.pushButton.setEnabled(False)
    	self.ui.statusBar.setText("Parsing file...")
    	self.parseThread.start()

    def startCounting(self):
    	self.ui.pushButton.setEnabled(False)
    	self.ui.output.setText("Statistics should be here in a moment...")
    	self.ui.statusBar.setText("Counting words occurences...")
    	self.countThread.start()

    def onCountingEnd(self):
    	self.ui.pushButton.setEnabled(True)
    	self.ui.statusBar.setText("Counting done!")
    	self.ui.output.setText(self.counter.getStatsByMonth())

    def onParsingEnd(self):
    	self.ui.pushButton.setEnabled(True)
    	self.ui.statusBar.setText("Parsing done!")

    def refreshCounterNames(self):
    	self.counter.namesChanged = True
    	self.counter.setYourName(str(self.ui.yourNameInput.text().toUtf8()).decode('utf-8'))
    	self.counter.setFriendsName(str(self.ui.yourFriendsNameInput.text().toUtf8()).decode('utf-8'))

    def refreshCounterWords(self):
    	wordsFromUi = str(self.ui.wordsInput.toPlainText().toUtf8()).decode('utf-8')
    	self.counter.words = [x.strip() for x in wordsFromUi.split(';')]

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())