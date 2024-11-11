import math

from MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.update)

    def show(self):
        self.MainWindow.show()

    def update(self):
        a = float(self.lineEditA.text())
        b = float(self.lineEditB.text())
        c = float(self.lineEditC.text())

        delta = float(b * b - 4 * a * c)
        if (a == 0):
            if (b == 0 and c != 0):
                x1 = x2 = "Vo nghiem"
            elif (b == 0 and c == 0):
                x1 = x2 = "Vo so nghiem"
            else:
                x = float(-c / b)
                x1 = x2 = x
        else:
            if (delta < 0):
                x1 = x2 = "Vo nghiem"
            elif (delta == 0):
                x1 = x2 = float(-b / 2 * a)
            else:
                x1 = float((-b + math.sqrt(delta)) / (2 * a))
                x2 = float((-b - math.sqrt(delta)) / (2 * a))

        self.lineEditX1.setText(f"{x1}")
        self.lineEditX2.setText(f"{x2}")