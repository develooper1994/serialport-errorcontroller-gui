from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QSizePolicy

class Ui_SerialBox(object):
    def setupUi(self, serialBox):
        serialBox.setObjectName("serialBox")
        button_horizontal = 210

        self.centralWidget = QtWidgets.QWidget(serialBox)
        self.centralWidget.setObjectName("centralWidget")

        # comboboxes
        self.portNamComboBox = QtWidgets.QComboBox(self.centralWidget)
        self.portNamComboBox.setGeometry(QtCore.QRect(520, 50, 181, 31))
        self.portNamComboBox.setObjectName("portNamComboBox")

        self.baudrateNamComboBox = QtWidgets.QComboBox(self.centralWidget)
        self.baudrateNamComboBox.setGeometry(QtCore.QRect(520, 100, 181, 31))
        self.baudrateNamComboBox.setObjectName("portNamComboBox")

        # labels
        self.port_name_label = QtWidgets.QLabel(self.centralWidget)
        self.port_name_label.setGeometry(QtCore.QRect(470, 50, 61, 31))
        self.port_name_label.setObjectName("port_name_label")

        self.baudrate_label = QtWidgets.QLabel(self.centralWidget)
        self.baudrate_label.setGeometry(QtCore.QRect(470, 100, 61, 31))
        self.baudrate_label.setObjectName("baudrate_label")

        self.SendBuffer_label = QtWidgets.QLabel(self.centralWidget)
        self.SendBuffer_label.setGeometry(QtCore.QRect(40, 360, 91, 16))
        self.SendBuffer_label.setObjectName("SendBuffer_label")

        self.sendTextEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.sendTextEdit.setGeometry(QtCore.QRect(150, 340, 301, 81))
        self.sendTextEdit.setObjectName("sendTextEdit")

        self.RecvBuffer_label = QtWidgets.QLabel(self.centralWidget)
        self.RecvBuffer_label.setGeometry(QtCore.QRect(40, 40, 91, 16))
        self.RecvBuffer_label.setObjectName("RecvBuffer_label")

        self.recvTextBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.recvTextBrowser.setGeometry(QtCore.QRect(150, 40, 301, 221))
        self.recvTextBrowser.setMouseTracking(False)
        self.recvTextBrowser.setObjectName("recvTextBrowser")

        self.sendTextButton = QtWidgets.QPushButton(self.centralWidget)
        self.sendTextButton.setGeometry(QtCore.QRect(500, 360, 93, 28))
        self.sendTextButton.setObjectName("sendTextButton")

        self.statusLabel = QtWidgets.QLabel(self.centralWidget)
        self.statusLabel.setGeometry(QtCore.QRect(470, button_horizontal + 100, 151, 21))
        self.statusLabel.setObjectName("statusLabel")

        # buttons
        self.openPortBtn = QtWidgets.QPushButton(self.centralWidget)
        self.openPortBtn.setGeometry(QtCore.QRect(510, button_horizontal, 101, 41))
        self.openPortBtn.setObjectName("openPortBtn")

        self.closePortBtn = QtWidgets.QPushButton(self.centralWidget)
        self.closePortBtn.setGeometry(QtCore.QRect(620, button_horizontal, 101, 41))
        self.closePortBtn.setObjectName("closePortBtn")

        self.clearBtn = QtWidgets.QPushButton(self.centralWidget)
        self.clearBtn.setGeometry(QtCore.QRect(20, 70, 101, 41))
        self.clearBtn.setObjectName("clearBtn")
        
        self.retranslateUi(serialBox)

        self.openPortBtn.clicked.connect(serialBox.open)
        self.closePortBtn.clicked.connect(serialBox.close)
        self.clearBtn.clicked.connect(serialBox.clear)
        self.recvTextBrowser.cursorPositionChanged.connect(serialBox.autoScroll)
        self.sendTextButton.clicked.connect(serialBox.write)

    def retranslateUi(self, serialBox):
        _translate = QtCore.QCoreApplication.translate
        serialBox.setTitle(_translate("SerialBox", "Serial Box"))
        self.port_name_label.setText(_translate("SerialBox", "Port: "))
        self.baudrate_label.setText(_translate("SerialBox", "Baudrate"))
        self.SendBuffer_label.setText(_translate("SerialBox", "SendBuffer:"))
        self.RecvBuffer_label.setText(_translate("SerialBox", "RecvBuffer:"))
        self.sendTextButton.setText(_translate("SerialBox", "Send"))
        self.statusLabel.setText(_translate("SerialBox", "Status: not  connect"))
        self.openPortBtn.setText(_translate("SerialBox", "Open"))
        self.closePortBtn.setText(_translate("SerialBox", "Close"))
        self.clearBtn.setText(_translate("SerialBox", "Clear"))
