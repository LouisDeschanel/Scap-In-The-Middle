import sys
from window import ScapyWindow
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
window = ScapyWindow(app)
sys.exit(app.exec_())