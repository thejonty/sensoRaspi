# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weatherDisplay.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(800, 480)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.label = QtGui.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(98, 104, 91, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.lcdNumber = QtGui.QLCDNumber(Frame)
        self.lcdNumber.setGeometry(QtCore.QRect(253, 92, 121, 41))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.calendarWidget = QtGui.QCalendarWidget(Frame)
        self.calendarWidget.setGeometry(QtCore.QRect(460, 40, 272, 165))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.graphicsView = QtGui.QGraphicsView(Frame)
        self.graphicsView.setGeometry(QtCore.QRect(470, 230, 256, 192))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.lcdNumber_2 = QtGui.QLCDNumber(Frame)
        self.lcdNumber_2.setGeometry(QtCore.QRect(255, 250, 121, 41))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.label_2 = QtGui.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(100, 262, 91, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textBrowser = QtGui.QTextBrowser(Frame)
        self.textBrowser.setGeometry(QtCore.QRect(120, 320, 256, 111))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.label.setText(_translate("Frame", "TextLabel", None))
        self.label_2.setText(_translate("Frame", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

