from MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.update)

    def show(self):
        self.MainWindow.show()

    def update(self):
        pass