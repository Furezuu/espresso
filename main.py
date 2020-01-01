import sqlite3
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5 import uic


class Espresso(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui')
        self.con = sqlite3.connect('coffee.sqlite')
        self.load_from_db()

    def load_from_db(self):
        cur = self.con.cursor()
        data = cur.execute('select * from coffees').fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHeadings('id', 'Название сорта', 'Степень прожарки', 'Молотый', 'Описание вкуса', 'Цена', 'Объём упаковки')
        for i in range(len(data)):
            for j in range(7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))
