import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar, QLineEdit, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile


class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        self.back_action = QAction("Back", self)
        self.toolbar.addAction(self.back_action)
        self.back_action.triggered.connect(self.go_back)

        self.url_bar = QLineEdit()
        self.toolbar.addWidget(self.url_bar)
        self.url_bar.returnPressed.connect(self.load_url)

        self.web_view.loadFinished.connect(self.update_url_bar)
        self.web_view.load(QUrl("https://www.google.com"))

    def go_back(self):
        if hasattr(self.web_view, 'history') and self.web_view.history().canGoBack():
            self.web_view.history().back()
        else:
            QMessageBox.information(self, "Cannot Go Back", "Cannot go back further.")


    def load_url(self):
        url = self.url_bar.text()
        if url.startswith("http://") or url.startswith("https://"):
            self.web_view.load(QUrl(url))
        else:
            QMessageBox.warning(self, "Invalid URL", "Please enter a valid URL starting with 'http://' or 'https://'.")

    def update_url_bar(self):
        url = self.web_view.url().toString()
        self.url_bar.setText(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.show()
    sys.exit(app.exec_())
