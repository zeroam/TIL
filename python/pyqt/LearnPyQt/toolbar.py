import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QToolBar,
    QAction,
    QStatusBar,
    QCheckBox,
)
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Jayone's Awesome App")

        label = QLabel('THIS IS AWESOME!!!')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon('bug.png'), 'Your button', self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        toolbar.addSeparator()

        button_action2 = QAction(QIcon('bug.png'), 'Your button2', self)
        button_action2.setStatusTip('This is your button2')
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(False)
        toolbar.addAction(button_action2)
        toolbar.addSeparator()

        toolbar.addWidget(QLabel('Hello'))
        toolbar.addSeparator()

        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print('click', s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()