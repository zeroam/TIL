import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # SIGNAL: The connected function will be called whenever
        # the window title is changed. The new title will be passed
        # to the function
        self.windowTitleChanged.connect(self.onWindowTitleChange)

        # SIGNAL
        # The new title is discarded in the lambda and the
        # function is called without parameter
        self.windowTitleChanged.connect(lambda x: self.my_custum_fn())

        # SIGNAL
        # The new title is passed to the function and
        # replaces the default parameter
        self.windowTitleChanged.connect(lambda x: self.my_custum_fn(x))

        # SIGNAL
        # The new title is passwd to the function and replaces
        # the default parameter. Extra data is passed from with
        # in lambda
        self.windowTitleChanged.connect(lambda x: self.my_custum_fn(x, 25))

        # This sets the window title which will trigger all the above
        # signals sending the new title to the attacted functins or lambdas
        # as the first parameter
        self.setWindowTitle("Jayone's Awesome App")

        label = QLabel('This is Awesome!!!')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

    # SLOT: This accepts a stiring, e.g. the window title, and prints it
    def onWindowTitleChange(self, s):
        print(s)

    # SLOT : This has default parameters and can be called without a value
    def my_custum_fn(self, a='HELLO!', b=5):
        print(a, b)

    # overriding event
    def contextMenuEvent(self, event):
        print('Context menu event!')
        super(MainWindow, self).contextMenuEvent(event)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

# start the event loop
app.exec_()
