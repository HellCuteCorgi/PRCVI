from PyQt6 import QtCore, QtGui, QtWidgets
from AddNoteWind import Ui_AddNoteWindow
from OpenFileWind import Ui_OpenFile

class Ui_MainWindow(object):

    def openAddNoteWind(self):
        self.window1 = QtWidgets.QMainWindow()
        self.ui = Ui_AddNoteWindow()
        self.ui.setupUi(self.window1)
        self.window1.show()

    def openEditNoteWind(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_AddNoteWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def openDeleteNoteWind(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = Ui_AddNoteWindow()
        self.ui.setupUi(self.window3)
        self.window3.show()

    def openOpenFileWind(self):
        self.window4 = QtWidgets.QMainWindow()
        self.ui = Ui_OpenFile()
        self.ui.setupUi(self.window4)
        self.window4.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 666)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("PT Sans Caption")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/logo_vert.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50;\n"
"    border: none;\n"
"    color: #fff;\n"
"    padding: 14px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 12px;\n"
"    margin: 4px 2px;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3e8e41\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 570, 1071, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddNote = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked = lambda: self.openAddNoteWind())
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.AddNote.setFont(font)
        self.AddNote.setStyleSheet("")
        self.AddNote.setObjectName("AddNote")
        self.horizontalLayout.addWidget(self.AddNote)
        self.EditNote = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked = lambda: self.openAddNoteWind())
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.EditNote.setFont(font)
        self.EditNote.setObjectName("EditNote")
        self.horizontalLayout.addWidget(self.EditNote)
        self.DeleteNote = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked = lambda: self.openAddNoteWind())
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.DeleteNote.setFont(font)
        self.DeleteNote.setObjectName("DeleteNote")
        self.horizontalLayout.addWidget(self.DeleteNote)
        self.OpenFile = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openAddNoteWind())
        self.OpenFile.setGeometry(QtCore.QRect(10, 260, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.OpenFile.setFont(font)
        self.OpenFile.setObjectName("OpenFile")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(196, 22, 851, 521))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PRCVI"))
        self.AddNote.setText(_translate("MainWindow", "Добавить запись"))
        self.EditNote.setText(_translate("MainWindow", "Изменить запись"))
        self.DeleteNote.setText(_translate("MainWindow", "Удалить запись"))
        self.OpenFile.setText(_translate("MainWindow", "Открыть файл"))
        self.label.setText(_translate("MainWindow", "ImageLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
