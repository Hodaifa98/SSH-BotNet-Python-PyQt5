#Import required modules.
from PyQt5 import QtCore, QtGui, QtWidgets

class HostObject:
    def __init__(self, host, username, password, port):
        self.host = host
        self.username = username
        self.password = password
        self.port = port

class Ui_addHostDialog(object):
    def addHostBtnClick(self):
        try:
            host = self.hostInput.text()
            username = self.usernameInput.text()
            password = self.passwordInput.text()
            port = self.portInput.text()
            hostObj = HostObject(host, username, password, port)
            self.cancelBtn.click()
        except Exception as ex:
            print(ex)

    def setupUi(self, addHostDialog):
        addHostDialog.setObjectName("addHostDialog")
        addHostDialog.resize(350, 170)
        addHostDialog.setMinimumSize(QtCore.QSize(350, 170))
        addHostDialog.setMaximumSize(QtCore.QSize(350, 170))
        self.buttonBox = QtWidgets.QDialogButtonBox(addHostDialog)
        self.buttonBox.setGeometry(QtCore.QRect(90, 120, 161, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(204, 246, 200);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(addHostDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 119))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.addHostForm = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.addHostForm.setContentsMargins(0, 0, 0, 0)
        self.addHostForm.setObjectName("addHostForm")
        self.hostLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.hostLabel.setObjectName("hostLabel")
        self.addHostForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.hostLabel)
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
        self.hostInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.hostInput.setObjectName("hostInput")
        self.addHostForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hostInput)

        self.retranslateUi(addHostDialog)
        self.buttonBox.accepted.connect(addHostDialog.accept)
        self.buttonBox.rejected.connect(addHostDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(addHostDialog)

    def retranslateUi(self, addHostDialog):
        _translate = QtCore.QCoreApplication.translate
        addHostDialog.setWindowTitle(_translate("addHostDialog", "Add a host"))
        self.hostLabel.setText(_translate("addHostDialog", "Host"))
        self.usernameLabel.setText(_translate("addHostDialog", "Username"))
        self.passwordLabel.setText(_translate("addHostDialog", "Password"))
        self.portLabel.setText(_translate("addHostDialog", "Port"))


#if __name__ == "__main__":
    #import sys
    #app = QtWidgets.QApplication(sys.argv)
    #addHostDialog = QtWidgets.QDialog()
    #ui = Ui_addHostDialog()
    #ui.setupUi(addHostDialog)
    #addHostDialog.show()
    #sys.exit(app.exec_())
