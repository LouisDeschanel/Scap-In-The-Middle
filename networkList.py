from PyQt5 import QtGui
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QAbstractItemView, QAction, QBoxLayout, QFormLayout, QLabel, QLineEdit, QMenu, QScrollArea, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QComboBox, QPushButton, qApp

class ScapyNetworkListWidget(QTableWidget):
    def __init__(self, windowManager):
        super().__init__()

        self.windowManager = windowManager
        self.cursorPos = QPoint()

        self.setWindowTitle("Network List")
        
        self.initWidget()
        self.initContextMenu()
    
    def initWidget(self):
        self.setColumnCount(3)
        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 200)
        self.setColumnWidth(2, 150)
        self.setHorizontalHeaderLabels(["IP", "Name", "MAC"])
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.verticalHeader().hide()

    def initContextMenu(self):
        self.menu = QMenu(self)        
        sendAction1 = QAction("Send to spoofer (1)", self)
        sendAction1.triggered.connect(lambda : self.sendToSpoofer(1))
        self.menu.addAction(sendAction1)   
        sendAction2 = QAction("Send to spoofer (2)", self)
        sendAction2.triggered.connect(lambda : self.sendToSpoofer(2))
        self.menu.addAction(sendAction2)

    def contextMenuEvent(self, event):
        if (self.rowCount() < 1):
            return
        self.menu.popup(QtGui.QCursor.pos())
        self.cursorPos = QtGui.QCursor.pos()
        
    def sendToSpoofer(self, slot):
        # print(self.rowAt(self.viewport().mapFromGlobal(QtGui.QCursor().pos()).y()))
        # print(self.item(0, 0).text())
        ip = self.item(self.rowAt(self.viewport().mapFromGlobal(self.cursorPos).y()), 0)
        mac = self.item(self.rowAt(self.viewport().mapFromGlobal(self.cursorPos).y()), 2)
        self.windowManager["Spoofer"].addToSpoof(ip.text(), mac.text(), slot)

    def populate(self, array):

        self.setRowCount(0)
        self.setRowCount(len(array))

        for i in range (0, len(array)):
            self.setItem(i, 0, QTableWidgetItem(array[i][0]))
            self.setItem(i, 1, QTableWidgetItem(array[i][1]))
            self.setItem(i, 2, QTableWidgetItem(array[i][2]))
