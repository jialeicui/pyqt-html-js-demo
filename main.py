#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSlot, QUrl, pyqtSignal, QFileInfo
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView

class CallHandler(QObject):
    result = pyqtSignal(str)

    @pyqtSlot(str,result=str)
    def test(self,foo):
        print("test recv: {}".format(foo))
        self.result.emit('hello from py({})'.format(foo))
        return 'py {}'.format(foo)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QWebEngineView()
    channel = QWebChannel()
    handler = CallHandler()
    channel.registerObject('pyjs', handler)
    view.page().setWebChannel(channel)
    url_string = QFileInfo("./index.html").absoluteFilePath()
    view.load(QUrl('file://{}'.format(url_string)))
    view.show()
    sys.exit(app.exec_())
