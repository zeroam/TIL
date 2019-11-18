import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow, 
    QDialog, 
    QDialogButtonBox,
    QPushButton,
    QVBoxLayout,
)


class CustomDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle('Hello!')

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Jayone's Awesome App")

        widget = QPushButton('Hello')
        widget.clicked.connect(self.onMyToolBarButtonClick)
        self.setCentralWidget(widget)

    def onMyToolBarButtonClick(self, s):
        print('click', s)

        dlg = CustomDialog(self)
        if dlg.exec_():
            print('Success')
        else:
            print('Cancel')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
