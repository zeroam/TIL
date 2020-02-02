import sys
import time
import json
import requests

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot

import design


class getPostsThread(QThread):
    add_post_signal = pyqtSignal(str)
    
    def __init__(self, subreddits):
        """
        Make a new thread instance with the specified
        subreddits as the first argument. The subreddits argument
        will be stored in an insatance variable called subreddits
        which then cab be accessed by all other class instance functions

        :param subreddits: A list of subreddit names
        :type subreddits: list
        """
        super().__init__()
        self.subreddits = subreddits

    def __del__(self):
        self.wait()

    def _get_top_post(self, subreddit):
        """
        Return a pre-formed string with top post title, author,
        and subreddit name from the subreddit passed as the only required
        argument

        :param subreddit: A valid subreddit name
        :type subreddit: str
        :return: A string with top post title, author, and
            subreddit name from that subreddit
        :rtype: str
        """
        url = f'https://www.reddit.com/r/{subreddit}.json?limit=1'
        headers = {'User-Agent': 'imdff0803@gmai.com for tutorial'}
        res = requests.get(url, headers=headers)
        data = json.loads(res.text)
        top_post = data['data']['children'][0]['data']
        return "'{title}' by {author} in {subreddit}".format(**top_post)

    def run(self):
        """
        Go over every item in the self.subreddits list
        (which was supplied during __init__)
        and for every item assume it's a string with valid subreddit
        name and fetch the top post using the _get_top_post method
        from reddit. Store the result in a local variable named
        top_post and then emit a SIGNAL add_post(QString) where
        QString is equal to the top_post variable that was set by the
        _get_top_post function
        """
        for subreddit in self.subreddits:
            top_post = self._get_top_post(subreddit)
            self.add_post_signal.emit(top_post)
            time.sleep(2)


class ThreadingTutorial(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_start.clicked.connect(self.start_getting_top_posts)

    def _get_top_post(self, subreddit):
        # Get the subreddits user entered into an QLineEdit field
        # this will be equal to '' if there is no text engtered
        url = f'https://www.reddit.com/r/{subreddit}.json?limit=1'
        headers = {'User-Agent': 'imdff0803@gmai.com for tutorial'}
        res = requests.get(url, headers=headers)
        data = json.loads(res.text)
        top_post = data['data']['children'][0]['data']
        return "'{title}' by {author} in {subreddit}".format(**top_post)

    def _get_top_from_subreddits(self, subreddits):
        for subreddit in subreddits:
            yield self._get_top_post(subreddit)
            time.sleep(2)

    def start_getting_top_posts(self):
        subreddit_list = str(self.edit_subreddits.text()).split(',')
        if subreddit_list == ['']:
            QtWidgets.QMessageBox.critical(self, "No subreddits",
                                           "You didn't enter any subreddits.",
                                           QtWidgets.QMessageBox.Ok)
            return

        # Set the maximum value of progress bar, can be any int and it will
        # be automatically converted to x/100% values
        # e.g. max_value = 3, current_value = 1, the progress bar will show 33%
        self.progress_bar.setMaximum(len(subreddit_list))
        # Setting the value on every run to 0
        self.progress_bar.setValue(0)

        # We have a list of subreddits which we use to create a new getPostsThread
        # instance and we pass that list to the thread
        self.get_thread = getPostsThread(subreddit_list)

        # Next we need to connect the events from that thread to functions we want
        # to be run when those signals get fired

        # Adding post will be handled in the add_post method and the signal that
        # the thread will emit is SIGNAL("add_post(QString)")
        # thre rest is same as we can use to connect any signal
        self.get_thread.add_post_signal.connect(self.add_post)

        # This is pretty self explanatory
        # regardless of whether the thread is finishes or the user terminates it
        # we want to show the notification to the user that adding is done
        # and regardless of whether it was terminated or finished by itself
        # the finished signal will be go off. So we don't need to catch the
        # terminated one specifically, but we could if we wanted
        self.get_thread.finished.connect(self.done)

        # We have all the events we need connected we can start the thread
        self.get_thread.start()
        # At this point we want to allow user to stop/terminate the thread
        # so we enable the button
        self.btn_stop.setEnabled(True)
        # And we connect the click of that button to the built in
        # terminate method that all QThread instances have
        self.btn_stop.clicked.connect(self.get_thread.terminate)
        # We don't want to enable user to start another thread while this one is
        # running so we disable the start button
        self.btn_start.setEnabled(False)

    def add_post(self, post_text):
        """
        Add the text that's given to this function to the
        list_submissions QListWidget we have in our GUI and
        increase the current value of preogress bar by 1

        :param post_text: text of the item to add to the list
        :type post_text
        """
        self.list_submissions.addItem(post_text)
        self.progress_bar.setValue(self.progress_bar.value() + 1)

    def done(self):
        """
        Show the message that fetching posts is done.
        Disable Stop button, enable the Start one and reset progress bar to 0
        """
        self.btn_stop.setEnabled(False)
        self.btn_start.setEnabled(True)
        self.progress_bar.setValue(0)
        QtWidgets.QMessageBox.information(self, "Done!", "Done fetching posts")


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ThreadingTutorial()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()