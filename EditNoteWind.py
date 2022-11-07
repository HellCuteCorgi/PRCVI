from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EditNote(object):
    def setupUi(self, EditNote):
        EditNote.setObjectName("EditNote")
        EditNote.resize(1080, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/logo_vert.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        EditNote.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(EditNote)
        self.centralwidget.setObjectName("centralwidget")
        EditNote.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditNote)
        QtCore.QMetaObject.connectSlotsByName(EditNote)

    def retranslateUi(self, EditNote):
        _translate = QtCore.QCoreApplication.translate
        EditNote.setWindowTitle(_translate("EditNote", "EditNoteWind"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditNote = QtWidgets.QMainWindow()
    ui = Ui_EditNote()
    ui.setupUi(EditNote)
    EditNote.show()
    sys.exit(app.exec())
