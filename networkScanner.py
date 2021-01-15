import scapy.all as scapy
import socket
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QBoxLayout, QFormLayout, QLabel, QLineEdit, QVBoxLayout, QWidget, QComboBox, QPushButton

class ScapyNetworkScannerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Network Scanner")
        layout = QVBoxLayout(self)

        layout.addWidget(self.addScanForm())
        layout.addWidget(self.addResult())

        self.setLayout(layout)
    
    def addScanForm(self):
        widget = QWidget()
        layout = QFormLayout()
        
        self.ip = QLineEdit()
        layout.addRow(QLabel("IP"), self.ip)

        self.range = QComboBox()
        self.range.addItems(["8", "16", "24"])
        layout.addRow(QLabel("Range"),  self.range)

        button = QPushButton("Scan")
        button.clicked.connect(self.networkScan)
        layout.addRow(button)

        widget.setLayout(layout)
        return (widget)
    
    def addResult(self):
        widget = QWidget()
        self.result = QVBoxLayout(widget)

        widget.setLayout(self.result)
        return (widget)
    
    def networkScan(self):
        print(socket.gethostbyaddr("192.168.1.1"))

        request = scapy.ARP() 
        request.pdst = self.ip.text() + '/' + self.range.currentText()
        broadcast = scapy.Ether() 
  
        broadcast.dst = 'ff:ff:ff:ff:ff:ff'
  
        request_broadcast = broadcast / request 
        clients = scapy.srp(request_broadcast, timeout = 1)[0] 
        for element in clients: 
            self.result.addWidget(QLabel(element[1].psrc))
            print(element[1].psrc + "      " + element[1].hwsrc) 