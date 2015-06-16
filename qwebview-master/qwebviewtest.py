import os
import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *
from PySide import QtWebKit

#Should be swapped with a read of a template
execfile('htmlfile.py')

def main():
    basepath = os.path.dirname(os.path.abspath(__file__))
    basepath = str(basepath)+'/'

    app = QApplication(sys.argv)
    win = QWebView()

    win.setWindowTitle('D3d visualziationt')
    layout = QVBoxLayout()
    win.setLayout(layout)

    view = QWebView()
    view.settings().setAttribute(QWebSettings.LocalContentCanAccessRemoteUrls, True)
    view.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)
    view.settings().setAttribute(QtWebKit.QWebSettings.WebAttribute.DeveloperExtrasEnabled, True)
    view.settings().setAttribute(QtWebKit.QWebSettings.PrivateBrowsingEnabled, True)


    view.setHtml(html, baseUrl=QUrl().fromLocalFile(basepath))

    # A button to call our JavaScript
    #button = QPushButton('Set Full Name')

    # Interact with the HTML page by calling the completeAndReturnName
    # function; print its return value to the console
    #def complete_name():
        #frame = view.page().mainFrame()
        #print frame.evaluateJavaScript('completeAndReturnName();')

    # Connect 'complete_name' to the button's 'clicked' signal
    #button.clicked.connect(complete_name)

    # Add the QWebView and button to the layout
    layout.addWidget(view)
    #layout.addWidget(button)

    # Show the window and run the app
    win.show()
    app.exec_()

if __name__ == '__main__':
    main()
