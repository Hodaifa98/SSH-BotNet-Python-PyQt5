#Import required modules.
#from pexpect import pxsshS
import sys
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from Design import ssh_window

botNet = []

class SSHBotNetApp:
    def __init__(self):
        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('ssh_botnet.ui')

        #3: Create the mainwindow
        self.mainwindow = builder.get_object('mainwindow')
        
    def run(self):
        self.mainwindow.mainloop()


class Client:
    #
    def __init__(self, host , user, password, port=22):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.session = self.connect()

    #
    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password, port=self.port)
            return s
        except Exception as ex:
            print("Error connecting...")
            print(ex)

    #
    def send_command(self, command):
        try:
            self.session.sendline(command)
            self.session.prompt()
            return self.session.before
        except Exception as ex:
            print(ex)

#
def sshbotnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print("Output from " + client.host)
        print(output)

#
def addClient(host, user, password, port=22):
    client = Client(host, user, password, port)
    botNet.append(client)

#
if __name__ == '__main__':
    #addClient("127.0.0.1", "osboxes", "osboxes.org")
    #sshbotnetCommand("ls")
    app = QtWidgets.QApplication(sys.argv)
    SSHBotNetWindow = QtWidgets.QMainWindow()
    ui = ssh_window.Ui_SSHBotNetWindow()
    ui.setupUi(SSHBotNetWindow)
    SSHBotNetWindow.show()
    sys.exit(app.exec_())