import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel, 
    QMainWindow, 
)
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Jayone's Awesome App")

        widget = QLabel('Hello')
        widget.setFixedSize(600, 600)
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # set image
        widget.setPixmap(QPixmap('python-large.jpg'))
        widget.setScaledContents(True)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()

