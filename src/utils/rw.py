"""Read/Write files util"""

import csv
import os
import time


def write_data_to_csv_file(file_path: str, data: list) -> None:
    """write data to file"""
    folder_name = os.path.dirname(file_path)
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)
        time.sleep(0.1)

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        file_writer = csv.writer(file, delimiter=";", lineterminator="\r")
        # for row in data:
        #     print("row")
        #     print(row)
        #     file_writer.writerow(row)
        file_writer.writerows(data)


def read_from_csv_file(file_path: str) -> list:
    """read data from file"""
    output_data = []

    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file, delimiter=";")
            for row in csv_reader:
                output_data.append(row)  # row будет списком значений

    return output_data
