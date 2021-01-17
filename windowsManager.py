from spoofer import ScapySpooferWidget
from networkList import ScapyNetworkListWidget
from networkScanner import ScapyNetworkScannerWidget
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMdiArea, QLabel, QMdiSubWindow, QVBoxLayout
from PyQt5.QtGui import QIcon, QValidator
from PyQt5.QtCore import Qt

window_dict = {
    "Network Scanner": ScapyNetworkScannerWidget,
    "Network List": ScapyNetworkListWidget,
    "Spoofer" : ScapySpooferWidget
}

class ScapyWindowsManager():
    def __init__(self, mainWindow):
        self.mdiAera = mainWindow.mdiAera
        self.windowContainer = mainWindow.windowContainer

    def __getitem__(self, key):
        if (not key in self.windowContainer):
            self.addSubWindow(window_dict[key](self))
        return (self.windowContainer[key])
    
    def addSubWindow(self, subWidget):
        subWindow = QMdiSubWindow()
        subWindow.setFixedHeight(500)
        subWindow.setFixedWidth(460)
        subWindow.setWidget(subWidget)
        subWindow.setAttribute(Qt.WA_DeleteOnClose)

        self.mdiAera.addSubWindow(subWindow)
        subWindow.show()
        self.windowContainer[subWindow.windowTitle()] = subWidget