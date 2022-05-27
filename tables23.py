from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem
import os
import sys
import sql_protocol
def right_number(a:list): 
    if int(a[1][3])<int(a[0][3])<int(a[2][3]):
        b = a[1]
        a.remove(a[1])
        a.insert(0,b)
    elif int(a[1][3])<int(a[2][3])<int(a[0][3]):   
        b= a[0]
        a.remove(a[0])
        a.insert(2,b)
    elif int(a[0][3])<int(a[2][3])<int(a[1][3]):    
        b= a[1]
        a.remove(a[1])
        a.insert(2,b)
    elif int(a[2][3])<int(a[0][3])<int(a[2][3]):    
        b = a[2]
        a.remove(a[2])
        a.insert(0,b)
    elif int(a[2][3])<int(a[1][3])<int(a[0][3]):
        a.reverse()   
    elif int(a[1][3]) == int(a[2][3])<int(a[0][3]):
        b = a[0]
        a.remove(a[0])
        a.insert(2,b)
    elif int(a[0][3])==int(a[2][3])<int(a[1][3]):
        b = a[1]
        a.remove(a[1])
        a.insert(2,b)
    elif int(a[0][3])==int(a[2][3])>int(a[1][3]):
        b = a[1]
        a.remove(a[1])
        a.insert(0,b)
    elif int(a[0][3])==int(a[1][3])>int(a[2][3]):
        b = a[2]
        a.remove(a[2])
        a.insert(0,b)    
    return a 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(598, 331)
        MainWindow.setWindowIcon(QtGui.QIcon('C:\\vscode\\project\\png\\icon.png'))
        MainWindow.setFixedSize(598, 331)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 50, 420, 120))

        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)

        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(3)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 280, 191, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.back_to_the_future)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 751, 331))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\vscode\\project\png\\reg.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()

        self.push_info = QtWidgets.QPushButton(self.centralwidget)
        self.push_info.setGeometry(QtCore.QRect(490,72, 30, 30))
        self.push_info.setIcon(QtGui.QIcon('C:\\vscode\\project\\png\\icon.png'))
        self.push_info.clicked.connect(self.text_info)

        self.push_info_2 = QtWidgets.QPushButton(self.centralwidget)
        self.push_info_2.setGeometry(QtCore.QRect(490,105, 30, 30))
        self.push_info_2.setIcon(QtGui.QIcon('C:\\vscode\\project\\png\\icon.png'))
        self.push_info_2.clicked.connect(self.text_info_2)

        self.push_info_3 = QtWidgets.QPushButton(self.centralwidget)
        self.push_info_3.setGeometry(QtCore.QRect(490,135, 30, 30))
        self.push_info_3.setIcon(QtGui.QIcon('C:\\vscode\\project\\png\\icon.png'))
        self.push_info_3.clicked.connect(self.text_info_3)

        self.tableWidget.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        self.right_name()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "  магазин"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", " цена "))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", " Название акции "))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "цена со скидкой"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Вернуться назад"))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger(0))
    def back_to_the_future(self):
        MainWindow.close()
        os.system("start C:\\vscode\\project\\main.exe")
    def right_name(self):
        with open('C:\\vscode\\project\\12.txt','r') as file:
            a = file.read()
            a = a.split('\n')
            for i in range(3):
                b = a[i]
                a.remove(a[i])
                b = b.split(' ')
                a.insert(i,b)   
            a = right_number(a)
            self.o = a   
            for i in range(len(a)):
                    for j in range(len(a[0])):
                        self.tableWidget.setItem(i,j,QTableWidgetItem(a[i][j]))                                   
    def text_info(self):
        with open('C:\\vscode\\project\\11.txt','r') as f:
            p = f.readline()    
        with open('C:\\vscode\\project\\32.txt','a') as file:
            file.write(f'{self.o[0][0]}\n{p}\n{self.o[0][3]}\n')
        
        dlg =QtWidgets.QMessageBox()
        dlg.setWindowTitle("Успешно")        
        dlg.setText('Товар добавлен в список покупок')
        dlg.exec()
    def text_info_2(self):
        with open('C:\\vscode\\project\\11.txt','r') as f:
            p = f.readline()    
        with open('C:\\vscode\\project\\32.txt','a') as file:
            file.write(f'{self.o[1][0]}\n{p}\n{self.o[1][3]}\n')
        
        dlg =QtWidgets.QMessageBox()
        dlg.setWindowTitle("Успешно")        
        dlg.setText('Товар добавлен в список покупок')
        dlg.exec()
    def text_info_3(self):
        with open('C:\\vscode\\project\\11.txt','r') as f:
            p = f.readline()    
        with open('C:\\vscode\\project\\32.txt','a') as file:
            file.write(f'{self.o[2][0]}\n{p}\n{self.o[2][3]}\n')
        
        dlg =QtWidgets.QMessageBox()
        dlg.setWindowTitle("Успешно")        
        dlg.setText('Товар добавлен в список покупок')
        dlg.exec()        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
