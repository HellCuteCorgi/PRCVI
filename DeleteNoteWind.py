from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DeleteNoteWind(object):
    def setupUi(self, DeleteNoteWind):
        DeleteNoteWind.setObjectName("DeleteNoteWind")
        DeleteNoteWind.resize(1080, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/logo_vert.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        DeleteNoteWind.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(DeleteNoteWind)
        self.centralwidget.setObjectName("centralwidget")
        DeleteNoteWind.setCentralWidget(self.centralwidget)

        self.retranslateUi(DeleteNoteWind)
        QtCore.QMetaObject.connectSlotsByName(DeleteNoteWind)

    def retranslateUi(self, DeleteNoteWind):
        _translate = QtCore.QCoreApplication.translate
        DeleteNoteWind.setWindowTitle(_translate("DeleteNoteWind", "DeleteNoteWind"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteNoteWind = QtWidgets.QMainWindow()
    ui = Ui_DeleteNoteWind()
    ui.setupUi(DeleteNoteWind)
    DeleteNoteWind.show()
    sys.exit(app.exec())
