import scapy.all as scapy
import socket
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QBoxLayout, QFormLayout, QLabel, QLineEdit, QScrollArea, QVBoxLayout, QWidget, QComboBox, QPushButton

class ScapyNetworkScannerWidget(QWidget):
    def __init__(self, windowsManager):
        self.windowsManager = windowsManager
        super().__init__()

        self.adjustSize()

        self.setWindowTitle("Network Scanner")

        layout = QVBoxLayout(self)

        layout.addWidget(self.addScanForm())

        self.setLayout(layout)
    
    def addScanForm(self):
        widget = QWidget()
        layout = QFormLayout()
        
        self.ip = QLineEdit()
        layout.addRow(QLabel("IP"), self.ip)

        self.range = QComboBox()
        self.range.addItems(["24", "16", "8"])
        layout.addRow(QLabel("Range"),  self.range)

        button = QPushButton("Scan")
        button.clicked.connect(self.networkScan)
        layout.addRow(button)

        widget.setLayout(layout)
        return (widget)

    def networkScan(self):
        result = []

        request = scapy.ARP() 
        request.pdst = self.ip.text() + '/' + self.range.currentText()
        broadcast = scapy.Ether() 
  
        broadcast.dst = 'ff:ff:ff:ff:ff:ff'
  
        request_broadcast = broadcast / request 
        clients = scapy.srp(request_broadcast, timeout = 5)[0] 
        for element in clients: 
            res = (element[1]. psrc, socket.gethostbyaddr(element[1].psrc)[0], element[1].hwsrc)
            result.append(res)
        self.windowsManager["Network List"].populate(result)