#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtGui
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("QT UI")
    window.show()
    sys.exit(app.exec_())