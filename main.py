from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QComboBox
import os

import sql_protocol
from sql_protocol import nameGoods
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('C:/vscode/project/png/icon.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 445)
        MainWindow.setFixedSize(788, 445)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -50, 791, 551))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAcceptDrops(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/vscode/project/png/main_theme.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        font = QtGui.QFont()
        font.setPointSize(10)


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(275, 90, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        self.combobox = QComboBox(self.centralwidget)
        self.combobox.setGeometry(QtCore.QRect(400, 90, 161, 31))
        self.combobox.setObjectName('combobox')
        self.combobox.addItems(nameGoods)


        self.Main_Script_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Main_Script_Button.setGeometry(QtCore.QRect(240, 200, 261, 41))
        self.Main_Script_Button.clicked.connect(self.open_new_window)

        self.list_button = QtWidgets.QPushButton(self.centralwidget)
        self.list_button.setGeometry(QtCore.QRect(500,200,80,41))
        self.list_button.setIcon(QtGui.QIcon('C:/vscode/project/png/icon.png'))
        self.list_button.clicked.connect(self.list_info)        

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Main_Script_Button.setFont(font)
        self.Main_Script_Button.setObjectName("Main_Script_Button")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shop-checker"))
        self.label_2.setText(_translate("MainWindow", "Shop-Checker"))
        self.label_4.setText(_translate("MainWindow", "Выберите товар:"))
        self.Main_Script_Button.setText(_translate("MainWindow", "Найти самые дешёвые цены"))
    def open_new_window(self):
        with open('C:/vscode/project/11.txt','w') as file:
            file.write(f'{self.combobox.currentText()}')   
        MainWindow.close()
        os.system('start C:/vscode/project/tables23.exe')
    def list_info(self):
        MainWindow.close()
        os.system('start C:/vscode/project/list_info.exe')
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
