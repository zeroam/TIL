from fbs_runtime.application_context.PyQt5 import (
    ApplicationContext,
    cached_property,
)
from PyQt5.QtWidgets import QMainWindow

import sys

class AppContext(ApplicationContext):       # 1. Subclass Application
    def run(self):                          # 2. Implement run()
        window = QMainWindow()
        version = self.build_settings['version']
        window.setWindowTitle('fbs v' + version)
        window.resize(250, 150)
        window.show()
        return self.app.exec_()             # 3. End run() with this

if __name__ == '__main__':
    appctxt = AppContext()                  # 4. Instantiate the subclass
    exit_code = appctxt.run()               # 5. Invoke run()
    sys.exit(exit_code)