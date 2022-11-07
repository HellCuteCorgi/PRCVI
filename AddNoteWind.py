from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddNoteWindow(object):
    def setupUi(self, AddNoteWindow):
        AddNoteWindow.setObjectName("AddNoteWindow")
        AddNoteWindow.resize(1080, 530)
        self.centralwidget = QtWidgets.QWidget(AddNoteWindow)
        self.centralwidget.setObjectName("centralwidget")
        AddNoteWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddNoteWindow)
        QtCore.QMetaObject.connectSlotsByName(AddNoteWindow)

    def retranslateUi(self, AddNoteWindow):
        _translate = QtCore.QCoreApplication.translate
        AddNoteWindow.setWindowTitle(_translate("AddNoteWindow", "AddNoteWind"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddNoteWindow = QtWidgets.QMainWindow()
    ui = Ui_AddNoteWindow()
    ui.setupUi(AddNoteWindow)
    AddNoteWindow.show()
    sys.exit(app.exec())
