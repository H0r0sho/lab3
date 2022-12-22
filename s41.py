import os
import csv
import re
import datetime
from typing import List, Optional


def next(path_to_csv: str, count: int) -> Optional[List[str]]:
    with open(path_to_csv + '/lab3/dataset.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile))
        if file_reader[count] is None:
            return None
        else:
            return file_reader[count]


def work_0(date: datetime.date,  path_to_csv: str=os.path.join("C:/", "Users", "79171", "PyCharmProjects")) -> str:
    "принимает данные, ищет их в файле соответствующего скрипта"
    with open(path_to_csv+'/lab3/dataset.csv', mode='r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            if (row[0] == str(date)):  # если одинаковые даты - выводим
                tmp = str(row[1])
                tmp = tmp.replace("[", "")
                tmp = tmp.replace("]", "")
                tmp = tmp.replace("'", "")
                return tmp
                
        else:
            return None


def work_1(date: datetime.date,  path_to_csv: str=os.path.join("C:/", "Users", "79171", "PyCharmProjects")) -> str:
    "принимает данные, ищет их в файле соответствующего скрипта"
    with open(path_to_csv +'/lab3/X.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile))
        for i in range(len(file_reader)):
            if (file_reader[i][0] == str( date)):  # ищем в фале Х запоминаем номер строки, выводим данные по номеру строки в фале Y
                value = i
                break
        else:
            return None
    with open(path_to_csv+'/lab3/Y.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile))
        tmp = str(file_reader[value])
        tmp = tmp.replace("[", "")
        tmp = tmp.replace("]", "")
        tmp = tmp.replace("'", "")
        return tmp



def work_2(date: datetime.date,  path_to_csv: str=os.path.join("C:/", "Users", "79171", "PyCharmProjects","lab3")) -> str:
    "принимает данные, ищет их в файле соответствующего скрипта"
    ways = os.listdir(path_to_csv)
    date = str(date)
    for i in range(len(ways)):
        if (ways[i][:4] == date[:4]):
            with open(path_to_csv + "/"+ ways[i], 'r', encoding='utf-8') as csvfile:
                file_reader = csv.reader(csvfile)
                for row in file_reader:
                    if (row[0] == date):
                        tmp = str(row[1])
                        tmp = tmp.replace("[", "")
                        tmp = tmp.replace("]", "")
                        tmp = tmp.replace("'", "")
                        return tmp
    else:
        return None


def work_3(date: datetime.date,  path_to_csv: str=os.path.join("C:/", "Users", "79171", "PyCharmProjects")) -> str:
    ways = os.listdir(path_to_csv+"/lab3/")
    list1 = []
    date = str(date)
    date = re.sub(r'[-]', '_', date)
    for i in range(len(ways)):  # выбираем одинаковые года и месяцы, записываем файлы в лист
        if (ways[i][:7] == date[:7]):
            list1.append(ways[i])
    if (list1 == None): return None
    for i in range(len(list1)):
        if (int(list1[i][11:13]) >= int(date[8:10]) >= int( list1[i][8:10])):  # если число находится в диапозоне недели то выводим его
            with open(path_to_csv + "/lab3/" + list1[i], 'r', encoding='utf-8') as csvfile:
                file_reader = csv.reader(csvfile)
                date = re.sub(r'[_]', '-', date)
                for row in file_reader:
                    if (row[0] == date):
                        tmp = str(row[1])
                        tmp = tmp.replace("[", "")
                        tmp = tmp.replace("]", "")
                        tmp = tmp.replace("'", "")
                        return tmp
    else:
        return None


def run_4(path_to_csv: str=os.path.join("C:/", "Users", "79171", "PyCharmProjects")) -> None:
    date = datetime.date()
    print(work_0(date, path_to_csv))
    print(work_1(date, path_to_csv))
    print(work_2(date, path_to_csv))
    print(work_3(date, path_to_csv))

    with open(path_to_csv+'/lab3/dataset.csv', 'r', encoding='utf-8') as csvfile:
        count = 0
        while (count != 54):
            next(path_to_csv, count)
            print(*next(path_to_csv, count))
            count += 1
