# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tom/workspace/MyPythonApplicationA/commonutils-for-python/commonutils/python2/RegexTester/cn/com/sunjiesh/regextester/ui/MainWin.ui'
#
# Created: Sat Aug 31 13:24:14 2013
#      by: PyQt4 UI code generator 4.10
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
        MainWindow.resize(800, 592)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, -10, 801, 601))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.textResult = QtGui.QTextBrowser(self.formLayoutWidget)
        self.textResult.setObjectName(_fromUtf8("textResult"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.textResult)
        self.textSource = QtGui.QTextEdit(self.formLayoutWidget)
        self.textSource.setObjectName(_fromUtf8("textSource"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.textSource)
        self.textPattern = QtGui.QTextEdit(self.formLayoutWidget)
        self.textPattern.setObjectName(_fromUtf8("textPattern"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.textPattern)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.btnRun = QtGui.QPushButton(self.formLayoutWidget)
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.btnRun)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Source", None))
        self.label_2.setText(_translate("MainWindow", "Pattern", None))
        self.label_3.setText(_translate("MainWindow", "Result", None))
        self.btnRun.setText(_translate("MainWindow", "Run", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

