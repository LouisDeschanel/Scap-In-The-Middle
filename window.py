import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMdiArea, QLabel, QMdiSubWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from toolbar import ScapyToolbar
from menuBar import ScapyMenuBar


class ScapyWindow(QMainWindow):
    
    def __init__(self, app):
        super(ScapyWindow, self).__init__()
        self.mdiAera = QMdiArea()
        self.app = app
        
        self.initWindow()
        self.setMenuBar(ScapyMenuBar(self))
        self.addToolBar(ScapyToolbar(self))

    def initWindow(self):
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('Scap in the middle')
        self.setWindowIcon(QIcon('web.png'))
        self.setCentralWidget(self.mdiAera)
        self.show()
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = ScapyWindow()
    sys.exit(app.exec_())