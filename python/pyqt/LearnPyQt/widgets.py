from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Jayone's Awesome App")

        layout = QVBoxLayout()
        widgets = [QCheckBox,
            QComboBox,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the window.
        # Widget will expand to take up all the space in the 
        # window by default
        self.setCentralWidget(widget)


# You need one (and only one) QApplication instance per application
# Pass in sys.argv to allow command line arguments for your app
# If you know you won't use commnand line arguments QApplication([]) works
app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!! window are hidden by default

# Start the event loop
app.exec_()

# Your application won't reach here until you exit and the event
# loop has stopped