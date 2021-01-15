from PyQt5.QtWidgets import QAction

class ToolbarButton(QAction):
    def __init__(self, name, function, window):
        super().__init__(name, window)
        self.triggered.connect(function)        