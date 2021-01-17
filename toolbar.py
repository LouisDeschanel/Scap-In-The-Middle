from spoofer import ScapySpooferWidget
from PyQt5.QtWidgets import QToolBar, QMdiArea, QMdiSubWindow, QLabel
from PyQt5.QtCore import Qt
from toolbarButton import ToolbarButton
from networkScanner import ScapyNetworkScannerWidget
from networkList import ScapyNetworkListWidget

class ScapyToolbar(QToolBar):
    def __init__(self, window):
        super().__init__("Main Toolbar")

        self.windowsManager = window.windowsManager

        self.addAction(ToolbarButton("Scanner", lambda: self.windowsManager.addSubWindow(ScapyNetworkScannerWidget(self.windowsManager)), window))
        self.addAction(ToolbarButton("Network", lambda: self.windowsManager.addSubWindow(ScapyNetworkListWidget(self.windowsManager)), window))
        self.addAction(ToolbarButton("Spoofer", lambda: self.windowsManager.addSubWindow(ScapySpooferWidget(self.windowsManager)), window))