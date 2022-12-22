import csv
import os


def run_1(path_to_csv: str=os.path.join("C:/", "Users", "79171", "PyCharmProjects")) -> None:
    list1 = []
    with open(path_to_csv + '/lab3/dataset.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            list1.append(row)

    with open(path_to_csv + "/lab3/X.csv", 'w', newline='', encoding='utf-8') as csvfile_x:
        for i in (range(0, len(list1))):
            all_data = [list1[i][0]]
            writer = csv.writer(csvfile_x)
            writer.writerow(all_data)

    with open(path_to_csv + "/lab3/Y.csv", 'w', newline='', encoding='utf-8') as csvfile_y:
        for i in range(0, len(list1)):
            all_data = [list1[i][1]]
            writer = csv.writer(csvfile_y)
            writer.writerow(all_data)