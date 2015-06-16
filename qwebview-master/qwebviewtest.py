import os
import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *
from PySide import QtWebKit

#Should be swapped with a read of a template
execfile('htmlfile.py')


class JavaScriptObject(QtCore.QObject):  
    """Simple class with one slot and one read-only property."""  
 
    @QtCore.pyqtSlot(str)  
    def showMessage(self, msg):  
        """Open a message box and display the specified message."""  
        QtGui.QMessageBox.information(None, "Info", msg)  
  
    def _pyVersion(self):  
        """Return the Python version."""  
        return sys.version  
  
    """Python interpreter version property."""  
    pyVersion = QtCore.pyqtProperty(str, fget=_pyVersion)  
  





def main():
    basepath = os.path.dirname(os.path.abspath(__file__))
    basepath = str(basepath)+'/'

    app = QApplication(sys.argv)
    win = QWebView()

    win.setWindowTitle('D3d visualization')
    layout = QVBoxLayout()
    win.setLayout(layout)

    view = QWebView()
    view.settings().setAttribute(QWebSettings.LocalContentCanAccessRemoteUrls, True)
    view.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)
    view.settings().setAttribute(QtWebKit.QWebSettings.WebAttribute.DeveloperExtrasEnabled, True)
    view.settings().setAttribute(QtWebKit.QWebSettings.PrivateBrowsingEnabled, True)


    var links = [
      {source: "Microsoft", target: "Amazon", type: "licensing"},
      {source: "Microsoft", target: "HTC", type: "licensing"},
      {source: "Samsung", target: "Apple", type: "suit"},
      {source: "Motorola", target: "Apple", type: "suit"},
      {source: "Nokia", target: "Apple", type: "resolved"},
      {source: "HTC", target: "Apple", type: "suit"},
      {source: "Kodak", target: "Apple", type: "suit"},
      {source: "Microsoft", target: "Barnes & Noble", type: "suit"},
      {source: "Microsoft", target: "Foxconn", type: "suit"},
      {source: "Oracle", target: "Google", type: "suit"},
      {source: "Apple", target: "HTC", type: "suit"},
      {source: "Microsoft", target: "Inventec", type: "suit"},
      {source: "Samsung", target: "Kodak", type: "resolved"},
      {source: "LG", target: "Kodak", type: "resolved"},
      {source: "RIM", target: "Kodak", type: "suit"},
      {source: "Sony", target: "LG", type: "suit"},
      {source: "Kodak", target: "LG", type: "resolved"},
      {source: "Apple", target: "Nokia", type: "resolved"},
      {source: "Qualcomm", target: "Nokia", type: "resolved"},
      {source: "Apple", target: "Motorola", type: "suit"},
      {source: "Microsoft", target: "Motorola", type: "suit"},
      {source: "Motorola", target: "Microsoft", type: "suit"},
      {source: "Huawei", target: "ZTE", type: "suit"},
      {source: "Ericsson", target: "ZTE", type: "suit"},
      {source: "Kodak", target: "Samsung", type: "resolved"},
      {source: "Apple", target: "Samsung", type: "suit"},
      {source: "Kodak", target: "RIM", type: "suit"},
      {source: "Nokia", target: "Qualcomm", type: "suit"}
    ];

    # Dynamic way to send javascript json objects to the html data



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
