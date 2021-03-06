#Import required modules.
import sys
import threading
import paramiko
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QSplashScreen, QLabel
from Design.add_host_dialog import Ui_addHostDialog

#
botNet_clients = []
host_threads = []

class Client:
    #
    def __init__(self, host, username, password, port=22):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        try:
            thread = threading.Thread(target=self.connectToHost)
            host_threads.append(thread)
            thread.start()
        except Exception as ex:
            print(ex)

    def connectToHost(self):
        self.session = self.connect()

    #
    def connect(self):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=self.host, username=self.username, password=self.password, port=self.port)
            return client
        except Exception as ex:
            print("Error connecting...")
            print(ex)

    #
    def send_command(self, command):
        try:
            pixmap = QPixmap("Design/loading.jpg")
            pixmap = pixmap.scaled(520, 350)
            splash = QSplashScreen(pixmap, Qt.WindowStaysOnTopHint)
            splash.show()
            splash.showMessage("")
            #Wait until all hosts have connected (or failed).
            [thread.join() for thread in host_threads]
            stdin, stdout, stderr = self.session.exec_command(command)
            #print(stderr.readlines())
            return stdout.readlines()
        except Exception as ex:
            print("Error executing commands...")
            print(ex)


def addClient(host, username, password, port=22):
    client = Client(host, username, password, port)
    botNet_clients.append(client)

def sshbotnetCommand(command):
    if len(botNet_clients) > 0 and len(command) > 0:
        results = []
        for client in botNet_clients:
            output = client.send_command(command)
            results.append("Output from: " + client.host)
            for s in output:
                results.append(s.split("\n")[0])
        return results
    else:
        return ""

class Ui_SSHBotNetWindow(object):
    def addHostToListAndRow(self, hostObj):
        addClient(hostObj.host, hostObj.username, hostObj.password, hostObj.port)
        rowPosition = self.hostsTable.rowCount()
        self.hostsTable.insertRow(rowPosition)
        self.hostsTable.setItem(rowPosition, 0, QTableWidgetItem(hostObj.host))
        self.hostsTable.setItem(rowPosition, 1, QTableWidgetItem(hostObj.username))
        self.hostsTable.setItem(rowPosition, 2, QTableWidgetItem(hostObj.port))
        

    def openAddHostDialog(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_addHostDialog()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        if dialog.result() == dialog.Accepted:
            hostObj = dialog.ui.getHostObj()
            self.addHostToListAndRow(hostObj)

    def removeHostsBtnClick(self):
        try:
            indices = sorted(self.hostsTable.selectionModel().selectedRows())
            for x in indices:
                del botNet_clients[x.row()]
                self.hostsTable.removeRow(x.row())
        except Exception as ex:
            print(ex)

    def executeCommand(self):
        output = sshbotnetCommand(self.commandTextInput.toPlainText())
        for s in output:
            res = self.commandTextInput.toPlainText() + "\n" + s
            self.commandTextInput.setText(res)

    def setupUi(self, SSHBotNetWindow):
        SSHBotNetWindow.setObjectName("SSHBotNetWindow")
        SSHBotNetWindow.resize(520, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SSHBotNetWindow.sizePolicy().hasHeightForWidth())
        SSHBotNetWindow.setSizePolicy(sizePolicy)
        SSHBotNetWindow.setMinimumSize(QtCore.QSize(520, 350))
        SSHBotNetWindow.setMaximumSize(QtCore.QSize(520, 350))
        self.hostsWidget = QtWidgets.QWidget(SSHBotNetWindow)
        self.hostsWidget.setObjectName("hostsWidget")
        self.hostsTable = QtWidgets.QTableWidget(self.hostsWidget)
        self.hostsTable.setGeometry(QtCore.QRect(10, 20, 501, 191))
        self.hostsTable.setObjectName("hostsTable")
        self.hostsTable.setColumnCount(3)
        self.hostsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.hostsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hostsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hostsTable.setHorizontalHeaderItem(2, item)
        #Disable editing cells.
        self.hostsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.addHostBtn = QtWidgets.QPushButton(self.hostsWidget)
        self.addHostBtn.setGeometry(QtCore.QRect(10, 220, 91, 23))
        self.addHostBtn.setStyleSheet("background-color: rgb(166, 244, 198);")
        self.addHostBtn.setObjectName("addHostBtn")
        #Click event for addHostBtn.
        self.addHostBtn.clicked.connect(self.openAddHostDialog)
        self.removeHostsBtn = QtWidgets.QPushButton(self.hostsWidget)
        self.removeHostsBtn.setGeometry(QtCore.QRect(10, 260, 91, 41))
        self.removeHostsBtn.setStyleSheet("background-color: rgb(213, 64, 98);\ncolor: rgb(255, 255, 255);")
        self.removeHostsBtn.setObjectName("removeHostsBtn")
        #Click event for removeHostsBtn.
        self.removeHostsBtn.clicked.connect(self.removeHostsBtnClick)
        self.executeBtn = QtWidgets.QPushButton(self.hostsWidget)
        self.executeBtn.setGeometry(QtCore.QRect(440, 260, 75, 23))
        self.executeBtn.setStyleSheet("background-color: rgb(0, 106, 113);\ncolor: rgb(255, 255, 255);")
        self.executeBtn.setObjectName("executeBtn")
        #Click event for executeBtn.
        self.executeBtn.clicked.connect(self.executeCommand)
        self.cmdToExecuteLabel = QtWidgets.QLabel(self.hostsWidget)
        self.cmdToExecuteLabel.setGeometry(QtCore.QRect(110, 230, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cmdToExecuteLabel.setFont(font)
        self.cmdToExecuteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cmdToExecuteLabel.setObjectName("cmdToExecuteLabel")
        self.commandTextInput = QtWidgets.QTextEdit(self.hostsWidget)
        self.commandTextInput.setGeometry(QtCore.QRect(210, 220, 221, 101))
        self.commandTextInput.setObjectName("commandTextInput")
        SSHBotNetWindow.setCentralWidget(self.hostsWidget)
        self.menuBar = QtWidgets.QMenuBar(SSHBotNetWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        self.fileMenu = QtWidgets.QMenu(self.menuBar)
        self.fileMenu.setObjectName("fileMenu")
        SSHBotNetWindow.setMenuBar(self.menuBar)
        self.importHostsMenuItem = QtWidgets.QAction(SSHBotNetWindow)
        self.importHostsMenuItem.setObjectName("importHostsMenuItem")
        self.exportHostsMenuItem = QtWidgets.QAction(SSHBotNetWindow)
        self.exportHostsMenuItem.setObjectName("exportHostsMenuItem")
        self.helpMenuItem = QtWidgets.QAction(SSHBotNetWindow)
        self.helpMenuItem.setObjectName("helpMenuItem")
        self.exitMenuItem = QtWidgets.QAction(SSHBotNetWindow)
        self.exitMenuItem.setObjectName("exitMenuItem")
        self.menuMenu.addAction(self.helpMenuItem)
        self.menuMenu.addAction(self.exitMenuItem)
        self.fileMenu.addAction(self.importHostsMenuItem)
        self.fileMenu.addAction(self.exportHostsMenuItem)
        self.menuBar.addAction(self.menuMenu.menuAction())
        self.menuBar.addAction(self.fileMenu.menuAction())
        self.retranslateUi(SSHBotNetWindow)
        QtCore.QMetaObject.connectSlotsByName(SSHBotNetWindow)

    def retranslateUi(self, SSHBotNetWindow):
        _translate = QtCore.QCoreApplication.translate
        SSHBotNetWindow.setWindowTitle(_translate("SSHBotNetWindow", "SSH BotNet"))
        item = self.hostsTable.horizontalHeaderItem(0)
        item.setText(_translate("SSHBotNetWindow", "Host"))
        item = self.hostsTable.horizontalHeaderItem(1)
        item.setText(_translate("SSHBotNetWindow", "Username"))
        item = self.hostsTable.horizontalHeaderItem(2)
        item.setText(_translate("SSHBotNetWindow", "Port"))
        self.addHostBtn.setText(_translate("SSHBotNetWindow", "Add a host"))
        self.removeHostsBtn.setText(_translate("SSHBotNetWindow", "Remove selected\nhosts"))
        self.executeBtn.setText(_translate("SSHBotNetWindow", "Execute"))
        self.cmdToExecuteLabel.setText(_translate("SSHBotNetWindow", "Command\nto execute"))
        self.menuMenu.setTitle(_translate("SSHBotNetWindow", "Menu"))
        self.fileMenu.setTitle(_translate("SSHBotNetWindow", "File"))
        self.importHostsMenuItem.setText(_translate("SSHBotNetWindow", "Import hosts"))
        self.exportHostsMenuItem.setText(_translate("SSHBotNetWindow", "Export hosts"))
        self.helpMenuItem.setText(_translate("SSHBotNetWindow", "Help"))
        self.exitMenuItem.setText(_translate("SSHBotNetWindow", "Exit"))

#
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    SSHBotNetWindow = QtWidgets.QMainWindow()
    ui = Ui_SSHBotNetWindow()
    ui.setupUi(SSHBotNetWindow)
    SSHBotNetWindow.show()
    sys.exit(app.exec_())