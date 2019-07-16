import os, sys, string

import platform

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSerialPort import QSerialPortInfo
from gui.ui_serialbox import Ui_SerialBox
from app.serialport import SerialPort


class SerialBox(QtWidgets.QGroupBox):
    """ Serial number edit box """

    def __init__(self, parent=None):
        super(SerialBox, self).__init__(parent)

        self.port = SerialPort()  # default baudrate is 57600 for this application
        self.port.serial.readyRead.connect(self.read)

        self.ui = Ui_SerialBox()
        self.ui.setupUi(self)
        self._setup_ui()

    def _setup_ui(self):
        """ """
        self.serialPortInfo()

    def serialPortInfo(self):
        port_list = QSerialPortInfo.availablePorts()
        baudrates = ['300', '1200', '2400', '9600', '19200', '57600', '115200']

        for port in port_list:
            self.ui.portNamComboBox.insertItem(0, port.portName())

        for br in baudrates:
            self.ui.baudrateNamComboBox.insertItem(0, br)

    def open(self):
        operating_system = platform.system()
        port_name = self.ui.port_comboBox.currentText()  # error occurs, # TODO! : fix the bug. Open button closes window
        if port_name == "":
            pass
        if operating_system == 'Linux':
            port_name = os.path.join("/dev", self.ui.port_comboBox.currentText())
        br = self.ui.baudrateNamComboBox.currentText()
        print("open port:", port_name)

        self.port.openSerial(port_name, br)  # TODO! : fix the bug. Open button closes window

    def close(self):
        self.port.closeSerial()

    def clear(self):
        self.ui.recvTextBrowser.clear()

    def write(self):
        data = self.ui.sendTextEdit.toPlainText()
        self.port.writeData(data)

    def read(self):
        data = self.port.readData()
        self.ui.recvTextBrowser.insertPlainText(data)
        self.ui.recvTextBrowser.insertPlainText("\n")

    def autoScroll(self):
        text_cursor = self.ui.recvTextBrowser.textCursor()
        text_cursor.movePosition(QtGui.QTextCursor.End)
        self.ui.recvTextBrowser.setTextCursor(text_cursor)
