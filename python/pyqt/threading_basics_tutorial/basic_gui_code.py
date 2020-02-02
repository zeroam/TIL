import sys
import time
import json
import requests

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread

import design


class ThreadingTutorial(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_start.clicked.connect(self.start_getting_top_posts)

    def _get_top_post(self, subreddit):
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

        self.progress_bar.setMaximum(len(subreddit_list))
        self.progress_bar.setValue(0)
        for top_post in self._get_top_from_subreddits(subreddit_list):
            self.list_submissions.addItem(top_post)
            self.progress_bar.setValue(self.progress_bar.value() + 1)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ThreadingTutorial()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()