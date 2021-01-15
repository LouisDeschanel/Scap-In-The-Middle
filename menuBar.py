from PyQt5.QtWidgets import QMenuBar, QAction, QMenu, QStyleFactory

class ScapyMenuBar(QMenuBar):
    def __init__(self, window):
        super().__init__()
        self.window = window
        displayMenu = self.addMenu('Display')
        themeMenu = QMenu('Theme', self)
        displayMenu.addMenu(themeMenu)

        for theme in QStyleFactory.keys():
            themeMenu.addAction(self.addThemeAction(theme))
    
    def addThemeAction(self, theme):
        themeAction = QAction(theme, self.window)
        themeAction.triggered.connect(lambda: self.changeScapyTheme(theme))
        return (themeAction)
    
    def changeScapyTheme(self, theme):
        print('ui')
        self.window.app.setStyle(theme)
        