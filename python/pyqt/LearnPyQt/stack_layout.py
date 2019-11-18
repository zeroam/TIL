import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QStackedLayout,
    QPushButton,
)
from PyQt5.QtGui import (
    QPalette,
    QColor,
)


class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.color_index = 3

        self.setWindowTitle("Jayone's Awesome App")

        layout = QVBoxLayout()
        layout2 = QStackedLayout()

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('green'))
        layout2.addWidget(Color('blue'))
        layout2.addWidget(Color('yellow'))

        layout2.setCurrentIndex(self.color_index)

        layout.addLayout(layout2)
        self.stack_layout = layout2

        push_button = QPushButton('change')
        push_button.clicked.connect(self.button_click)
        layout.addWidget(push_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def button_click(self):
        self.color_index += 1
        if self.color_index > 3:
            self.color_index = 0
        self.stack_layout.setCurrentIndex(self.color_index)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
