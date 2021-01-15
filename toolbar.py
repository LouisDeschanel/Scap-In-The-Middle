from PyQt5.QtWidgets import QToolBar, QMdiArea, QMdiSubWindow, QLabel
from PyQt5.QtCore import Qt
from toolbarButton import ToolbarButton
from networkScanner import ScapyNetworkScannerWidget

class ScapyToolbar(QToolBar):
    def __init__(self, window):
        super().__init__("Main Toolbar")
        self.window = window
        self.addAction(ToolbarButton("NetworkScanner", lambda: self.addSubWindow(ScapyNetworkScannerWidget()), window))

    def addSubWindow(self, subWidget):
        subWidget.setFixedWidth(200)
        subWidget.setFixedHeight(200)
        
        subWindow = QMdiSubWindow()
        subWindow.setWidget(subWidget)
        subWindow.setAttribute(Qt.WA_DeleteOnClose)
        self.window.mdiAera.addSubWindow(subWindow)
        subWindow.show()