from PyQt5 import QtWidgets, uic
import pyqtgraph as pg
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Load the UI page
        uic.loadUi('mainwindow.ui', self)

        self.plot(range(1, 11), [30, 32, 34, 32, 33, 31, 29, 32, 35, 45])


    def plot(self, hour, temperature):
        self.graphWidget.plot(hour, temperature)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()