import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem)

class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('designer_for_coffee.ui', self)

        # Запуск функции load_table_data
        self.load_table_data()

    def load_table_data(self):
        # Создаем соединение с базой данных
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()

        # Извлекаем данные из базы данных
        cursor.execute('SELECT id, название, степень_обжарки, молотый_или_в_зернах, описание_вкуса, цена, объем_упаковки FROM coffee_table')
        coffee_table = cursor.fetchall()

        # Проверяем, что coffee_table не пустой
        if coffee_table:
            # Очищаем таблицу перед обновлением
            self.table_widget.setRowCount(0)
            self.table_widget.setColumnCount(0)

            # Устанавливаем количество строк и столбцов в таблице
            self.table_widget.setRowCount(len(coffee_table))
            self.table_widget.setColumnCount(len(coffee_table[0]))

            # Заполняем таблицу данными из базы данных
            for row, coffee in enumerate(coffee_table):
                for column, data in enumerate(coffee):
                    item = QTableWidgetItem(str(data))
                    self.table_widget.setItem(row, column, item)
        else:
            print("База данных пуста")

if __name__ == '__main__':
    app = QApplication([])
    window = Coffee()
    window.show()
    app.exec_()