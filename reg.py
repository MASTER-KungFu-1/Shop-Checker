from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import *
import os
import sys
import pymysql

class Ui_MainWindow(object):
 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 330)
                                           
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowIcon(QtGui.QIcon('C:/vscode/project/png/icon.png'))
        MainWindow.setFixedSize(595,330)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-6, -1, 611, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.log_in = QtWidgets.QWidget()
        self.log_in.setObjectName("log_in")
        self.label_2 = QtWidgets.QLabel(self.log_in)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 611, 311))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/vscode/project/png/reg.jpg"))
        self.label_2.setObjectName("label_2")
        self.Login_Log_in = QtWidgets.QPlainTextEdit(self.log_in)
        self.Login_Log_in.setGeometry(QtCore.QRect(260, 50, 100, 27))
        self.Login_Log_in.setObjectName("Login_Log_in")
        self.Password_log_in = QtWidgets.QLineEdit(self.log_in)
        self.Password_log_in.setGeometry(QtCore.QRect(260, 80, 100, 27))
        self.Password_log_in.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.Password_log_in.setObjectName("Password_log_in")
        self.Log_in = QtWidgets.QPushButton(self.log_in)
        self.Log_in.setGeometry(QtCore.QRect(260, 110, 101, 28))
        self.Log_in.setObjectName("Log_in")
        self.Log_in.clicked.connect(self.Log_in_info)
        self.tabWidget.addTab(self.log_in, "")
        self.Reg = QtWidgets.QWidget()
        self.Reg.setObjectName("Reg")
        self.label = QtWidgets.QLabel(self.Reg)
        self.label.setGeometry(QtCore.QRect(4, -5, 601, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/vscode/project/png/reg.jpg"))
        self.label.setObjectName("label")
        self.Login_sign_up = QtWidgets.QPlainTextEdit(self.Reg)
        self.Login_sign_up.setGeometry(QtCore.QRect(260, 50, 100, 27))
        self.Login_sign_up.setObjectName("Login_sign_up")
        self.Password_sign_up = QtWidgets.QLineEdit(self.Reg)
        self.Password_sign_up.setGeometry(QtCore.QRect(260, 80, 100, 27))
        self.Password_sign_up.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.Password_sign_up.setObjectName("Password_sign_up")
        self.Sign_up = QtWidgets.QPushButton(self.Reg)
        self.Sign_up.setGeometry(QtCore.QRect(260, 110, 100, 27))
        self.Sign_up.clicked.connect(self.sign_in)
        self.Sign_up.setObjectName("Sign_up")
        self.tabWidget.addTab(self.Reg, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вход"))
        self.Login_Log_in.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.Password_log_in.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.Log_in.setText(_translate("MainWindow", "Войти"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log_in), _translate("MainWindow", "Log in"))
        self.Login_sign_up.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.Password_sign_up.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.Sign_up.setText(_translate("MainWindow", "Войти"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Reg), _translate("MainWindow", "Sign up"))
    def sign_in(self):
        login = self.Login_sign_up.toPlainText()
        password = self.Password_sign_up.text()
        with open("C:/vscode/project/info.txt","r") as file:
            a = file.read().split()
        
        if login == '' or login == 'Логин':
            dlg =QtWidgets.QMessageBox()
            dlg.setWindowTitle("Ошибка")        
            dlg.setText('Введите Логин!')
            dlg.exec()
        elif login in a:
            dlg =QtWidgets.QMessageBox()
            dlg.setWindowTitle("Ошибка")        
            dlg.setText('Данный логин уже занят!')
            dlg.exec()
        elif password =='' or password == 'Пароль':
            dlg =QtWidgets.QMessageBox()
            dlg.setWindowTitle("Ошибка")        
            dlg.setText('Введите пароль!')
            dlg.exec()
        else:
            with open("C:/vscode/project/info.txt","a") as file:
                file.write(f"{login} {password}\n")
            
            MainWindow.close()
            dlg =QtWidgets.QMessageBox()
            dlg.setWindowTitle("Успех")        
            dlg.setText('Вы успешно зарегистрировались')
            dlg.exec()
            os.system("start C:/Users/srezv/OneDrive/Desktop/reg.exe")      #!
        
    def Log_in_info(self):
        file = open('C:/vscode/project/info.txt','r')
        info = str(file.readlines()).split()
        login = str(self.Login_Log_in.toPlainText())
        password = str(self.Password_log_in.text())

        for i in range(len(info)):
            while "'" in info[i] or "\n" in info[i] or "\\n" in info[i] or "[" in info[i] or "]" in info[i] or ',' in info[i]:
                if "'" in info[i]:
                    a = info[i].replace("'",'')
                    info.remove(info[i])
                    info.insert(i,a)
                elif "\n" in info[i]:
                    a = info[i].replace("\n",'')
                    info.remove(info[i])
                    info.insert(i,a)
                elif "\\n" in info[i]:
                    a = info[i].replace("\\n",'')
                    info.remove(info[i])
                    info.insert(i,a)
                elif "[" in info[i]:
                    a = info[i].replace("[",'')
                    info.remove(info[i])
                    info.insert(i,a)   
                elif "]" in info[i]:
                    a = info[i].replace("]",'')
                    info.remove(info[i])
                    info.insert(i,a)     
                elif ',' in info[i]:
                    a = info[i].replace(",",'')
                    info.remove(info[i])
                    info.insert(i,a)                        
        for i in range(0,len(info),2):
            if info[i]==login:
                if info[i+1] == password:
                    self.open_new_window()
                    break
                else:
                    dlg =QtWidgets.QMessageBox()
                    dlg.setWindowTitle("Ошибка")        
                    dlg.setText('Неправильно введён логин или пароль!')
                    dlg.exec()
                    break     
        if login not in info:
            dlg =QtWidgets.QMessageBox()
            dlg.setWindowTitle("Ошибка")        
            dlg.setText('Неправильно введён логин или пароль!')
            dlg.exec()  
    def open_new_window(self):
        MainWindow.close()
        os.system("start C:/vscode/project/main.exe")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
