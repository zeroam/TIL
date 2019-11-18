import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Jayone's Awesome App")

        widget = QListWidget()
        widget.addItems(['One', 'Two', 'Three'])

        # In QListWidget there are two separate signals for the item,
        # and str
        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):     # Not an index, i is a QListItem
        print(i.text())

    def text_changed(self, s):
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
