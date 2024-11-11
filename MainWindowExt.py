import math

from PyQt6.QtWidgets import QMessageBox

from FunctionUtils import ptb2
from MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.update)

    def show(self):
        self.MainWindow.show()

    def update(self):
        x1,x2 = "",""
        try:
            a = float(self.lineEditA.text())
            b = float(self.lineEditB.text())
            c = float(self.lineEditC.text())
            x1,x2= ptb2(a,b,c)
        except:
            dlg = QMessageBox(self.MainWindow)
            dlg.setWindowTitle("Lỗi dữ liệu")
            dlg.setText("Chỉ được nhập số cho a, b, c")
            dlg.setStandardButtons(QMessageBox.StandardButton.Close)
            dlg.setIcon(QMessageBox.Icon.Warning)
            button = dlg.exec()
            # check the user confirmation
            button = QMessageBox.StandardButton(button)
            if button == QMessageBox.StandardButton.Close:
                dlg.close()
            else:
                pass

        self.lineEditX1.setText(f"{x1}")
        self.lineEditX2.setText(f"{x2}")