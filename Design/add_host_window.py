#Import required modules.
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddHostWindow(object):
    def cancelAddHost(self):
        self.close()
    def setupUi(self, AddHostWindow):
        AddHostWindow.setObjectName("AddHostWindow")
        AddHostWindow.resize(350, 215)
        AddHostWindow.setMinimumSize(QtCore.QSize(350, 215))
        AddHostWindow.setMaximumSize(QtCore.QSize(350, 215))
        self.addHostWidget = QtWidgets.QWidget(AddHostWindow)
        self.addHostWidget.setObjectName("addHostWidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.addHostWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 331, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.addHostForm = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.addHostForm.setContentsMargins(0, 0, 0, 0)
        self.addHostForm.setObjectName("addHostForm")
        self.hostLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.hostLabel.setObjectName("hostLabel")
        self.addHostForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.hostLabel)
        self.hostInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.hostInput.setObjectName("hostInput")
        self.addHostForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hostInput)
        self.usernameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.addHostForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usernameInput.setObjectName("usernameInput")
        self.addHostForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.usernameInput)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.addHostForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwordInput.setInputMask("")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.addHostForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwordInput)
        self.portLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.portLabel.setObjectName("portLabel")
        self.addHostForm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.portLabel)
        self.portInput = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.portInput.setMinimum(1)
        self.portInput.setMaximum(65535)
        self.portInput.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.portInput.setProperty("value", 22)
        self.portInput.setObjectName("portInput")
        self.addHostForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.portInput)
        self.addHostBtn = QtWidgets.QPushButton(self.addHostWidget)
        self.addHostBtn.setGeometry(QtCore.QRect(140, 150, 75, 23))
        self.addHostBtn.setStyleSheet("background-color: rgb(204, 246, 200);")
        self.addHostBtn.setObjectName("addHostBtn")
        self.cancelBtn = QtWidgets.QPushButton(self.addHostWidget)
        self.cancelBtn.setGeometry(QtCore.QRect(140, 180, 75, 23))
        self.cancelBtn.setStyleSheet("background-color: rgb(213, 64, 98);\n"
"color: rgb(255, 255, 255);")
        self.cancelBtn.setObjectName("cancelBtn")
        #Click event for cancelBtn.
        self.cancelBtn.clicked.connect(self.cancelAddHost)
        AddHostWindow.setCentralWidget(self.addHostWidget)

        self.retranslateUi(AddHostWindow)
        QtCore.QMetaObject.connectSlotsByName(AddHostWindow)

    def retranslateUi(self, AddHostWindow):
        _translate = QtCore.QCoreApplication.translate
        AddHostWindow.setWindowTitle(_translate("AddHostWindow", "Add a host"))
        self.hostLabel.setText(_translate("AddHostWindow", "Host"))
        self.usernameLabel.setText(_translate("AddHostWindow", "Username"))
        self.passwordLabel.setText(_translate("AddHostWindow", "Password"))
        self.portLabel.setText(_translate("AddHostWindow", "Port"))
        self.addHostBtn.setText(_translate("AddHostWindow", "Add host"))
        self.cancelBtn.setText(_translate("AddHostWindow", "Cancel"))


#if __name__ == "__main__":
    #import sys
    #app = QtWidgets.QApplication(sys.argv)
    #AddHostWindow = QtWidgets.QMainWindow()
    #ui = Ui_AddHostWindow()
    #ui.setupUi(AddHostWindow)
    #AddHostWindow.show()
    #sys.exit(app.exec_())
