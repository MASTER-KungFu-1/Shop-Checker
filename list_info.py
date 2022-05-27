from dataclasses import replace
from PyQt6 import QtCore, QtGui, QtWidgets
import os
from PyQt6.QtWidgets import QTableWidgetItem

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('C:\\vscode\\project\\png\\icon.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 335)
        MainWindow.setFixedSize(360, 335)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 360, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1,130)
        self.tableWidget.setColumnWidth(2,60)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(20, 300, 100, 31))
        self.btn_back.clicked.connect(self.back)

        self.itog = QtWidgets.QLabel(self.centralwidget)
        self.itog.setGeometry(QtCore.QRect(125, 300, 200, 31))
        self.itog.setStyleSheet('Color: orange;')
        self.itog.setText("итоговая цена: 13312")
        

        self.btn_list = QtWidgets.QPushButton(self.centralwidget)
        self.btn_list.setGeometry(QtCore.QRect(257, 300, 100, 31))
        self.btn_list.clicked.connect(self.clear_list)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Script()
        self.Itog()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shop-checker"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Магазин"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Товар"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Цена"))
        self.btn_back.setText(_translate("MainWindow", "Вернуться назад"))
        self.btn_list.setText(_translate("MainWindow", "Очистить"))
    def back(self):
        MainWindow.close()
        os.system('start C:\\vscode\\project\\main.exe')
    def Script(self):
        with open('C:\\vscode\\project\\32.txt','r') as file:
            self.a =[]
            i =0
            j =0
            for x in file:
                if j==3:
                    i+=1
                    j=0
                self.a.append(str(x).replace('\n',''))
                self.tableWidget.setItem(i,j,QTableWidgetItem(str(x).replace('\n','')))
                j+=1
    def clear_list(self):
        with open('C:\\vscode\\project\\32.txt','w') as file:
            file.write('')           
             
        MainWindow.close()
        dlg =QtWidgets.QMessageBox()
        dlg.setWindowTitle("Успешно")        
        dlg.setText('Вы успешно очистили список покупок')
        dlg.exec()     
        os.system('start C:\\vscode\\project\\list_info.exe')
    def Itog(self):
        self.p = 0
        for i in range(2,len(self.a),3):
           self.p += int(self.a[i]) 
        self.itog.setText('Итоговая цена = '+str(self.p))   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
