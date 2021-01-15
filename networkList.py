from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QBoxLayout, QFormLayout, QLabel, QLineEdit, QScrollArea, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QComboBox, QPushButton

class ScapyNetworkListWidget(QTableWidget):
    def __init__(self, windowManager):
        super().__init__()

        self.windowManager = windowManager

        self.setWindowTitle("Network List")
        self.setColumnCount(3)
        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 200)
        self.setColumnWidth(2, 150)
        self.setHorizontalHeaderLabels(["IP", "Name", "MAC"])
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.verticalHeader().hide()
    def populate(self, array):

        self.setRowCount(0)
        self.setRowCount(len(array))

        for i in range (0, len(array)):
            self.setItem(i, 0, QTableWidgetItem(array[i][0]))
            self.setItem(i, 1, QTableWidgetItem(array[i][1]))
            self.setItem(i, 2, QTableWidgetItem(array[i][2]))
