import sys
import datetime
import os

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QWidget, QPushButton, QInputDialog
from PyQt5.QtGui import QPixmap

import s11
import s21
import s31
import s41


class Window2(QWidget):
    def __init__(self, date: datetime.date, path_to_csv: os.path ) -> None:
        super().__init__()

        self.setGeometry(500, 500, 500, 500)
        self.background_2 = QLabel(self)
        self.fire = QLabel(self)
        self.setWindowTitle('Выбор файла')

        self.base = QtWidgets.QLabel(self)
        self.base.setFont(QtGui.QFont("Times", 11, QtGui.QFont.Light))
        self.base.setText("Найти данные в файле по...")
        self.base.move(100, 10)
        self.base.setStyleSheet("background-color: white; border: 1px solid black;")
        self.base.adjustSize()

        self.b2_1 = QPushButton('Дата/Данные', self)
        self.b2_1.resize(150, 80)
        self.b2_1.move(170, 100)
        self.b2_1.clicked.connect(lambda: self.findbydate_data(date))

        self.b2_2 = QPushButton('Годам', self)
        self.b2_2.resize(150, 80)
        self.b2_2.move(170, 180)
        self.b2_2.clicked.connect(lambda: self.findbyyears(date))

        self.b2_3 = QPushButton('Неделям', self)
        self.b2_3.resize(150, 80)
        self.b2_3.move(170, 260)
        self.b2_3.clicked.connect(lambda: self.findbyweek(date))

        self.b2_4 = QPushButton('dataset', self)
        self.b2_4.resize(150, 80)
        self.b2_4.move(170, 340)
        self.b2_4.clicked.connect(lambda: self.findbydataset(date))


def findbydatedata(self, date: datetime.date) -> None:
    tmp = s41.work_1(date)
    QMessageBox.about(self, "Информация по дате", f"Дата: {date} \nДанные : {tmp}")


def findbyyears(self, date: datetime.date) -> None:
    tmp = s41.work_2(date)
    QMessageBox.about(self, "Информация по дате", f"Дата: {date} \nДанные : {tmp}")


def findbyweek(self, date: datetime.date) -> None:
    tmp = s41.work_3(date)
    QMessageBox.about(self, "Информация по дате", f"Дата: {date} \n Данные : {tmp}")


def findbydataset(self, date: datetime.date) -> None:
    tmp = s41.work_0(date)
    QMessageBox.about(self, "Информация по дате", f"Дата: {date} \nДанные : {tmp}")


class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        path_to_csv = os.path.join("C:/", "Users", "79171", "PyCharmProjects", "lab3")
        super(Window, self).__init__()
        self.setFixedSize(600, 500)
        self.setWindowTitle("Value by Dates")
        self.background = QLabel(self)
        self.fire = QLabel(self)

        self.base = QtWidgets.QLabel(self)
        self.base.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        self.base.setText("Создание и выбор аннотаций")
        self.base.move(130, 10)
        self.base.adjustSize()

        self.folderpath_dataset = ""
        while self.folderpath_dataset == "":
            self.folderpath_dataset = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Please select folder of dataset"
            )

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Разделение на года")
        self.b1.setFixedSize(200, 50)
        self.b1.move(200, 100)
        self.b1.clicked.connect(self.sort_year)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Разделение на недели")
        self.b2.setFixedSize(200, 50)
        self.b2.move(200, 150)
        self.b2.clicked.connect(self.sort_week)

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Разделение на даты и данные")
        self.b3.setFixedSize(200, 50)
        self.b3.move(200, 200)
        self.b3.clicked.connect(self.sort_data_date)

        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("Ввести дату")
        self.b4.setFixedSize(200, 50)
        self.b4.move(200, 300)
        self.b4.clicked.connect(self.input_data)

    def sort_data_date(self) -> None:
        s11.run_1()
        QMessageBox.about(self, "Sort", "Sorting by date")

    def sort_week(self) -> None:
        s31.run_3()
        QMessageBox.about(self, "Sort", "Sorting by week")

    def sort_year(self) -> None:
        s21.run_2()
        QMessageBox.about(self, "Sort", "Sorting by year")
    def check_date(self, text: str) -> bool:
        Flag = False
        check, check_value = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"], ["0", "1", "3", "4", "6", "7", "8", "9"]
        if  len(text) != 10: return False
        for i in range(len(check_value)):
           for j in range(len(check)):
                if text[int(check_value[i])] == check[j]: Flag = True
           if Flag == False: return False
        if (0 <= int(text[0:2]) <= 31 and 0 <= int(text[3:5]) <= 12 and 1992 <= int(text[6:10]) <= 2022): return True
        else: return False

    def input_data(self) -> None:
        """a function that accepts a date and checks it for correctness"""
        text, ok = QInputDialog.getText(self, 'Data', 'Enter the data in the format dd.mm.yyyy:')
        dictionary = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if ok:
            if self.check_date(text) == True:
                        if  int(text[0:2])<=dictionary[int(text[3:5])-1]:
                            date = datetime.date(int(text[6:10]), int(text[3:5]), int(text[0:2]))
                            self.show_window_2(date)
                        else:  QMessageBox.about(self, "warning!\n", "Неправильные данные...")
            else:  QMessageBox.about(self, "warning!\n", "Неправильный формат входных данных...")


    def show_window_2(self, date: datetime.date) -> None:
        self.w2 = Window2(date, path_to_csv = os.path.join("C:/", "Users", "79171", "PyCharmProjects", "lab3"))
        self.w2.show()

def application() -> None:
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #run_1()
    #run_2()
    #run_3()
    #run_4()
    application()