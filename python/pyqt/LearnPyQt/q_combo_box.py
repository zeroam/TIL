import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QComboBox,
)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Jayone's Awesome App")

        widget = QComboBox()
        widget.addItems(['One', 'Two', 'Three'])
        widget.addItem('Four')

        # can be editable with this option
        widget.setEditable(True)

        widget.setInsertPolicy(QComboBox.InsertAlphabetically)
        widget.setMaxCount(10)

        # The default signal from currentIndexChanged sends the index
        widget.currentIndexChanged.connect(self.index_changed)

        # The same signal can send a text string
        widget.currentIndexChanged[str].connect(self.text_changed)
        

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()