import csv
import sys

def search(poetry_line):
    csv_file = csv.reader(open('output.csv', mode="r", encoding="utf-8"), delimiter=",")
    for row in csv_file:
        if poetry_line == row[0]:
            return row[1]
    return None


if __name__ == "__main__":
    search_res = search("床前明月光，疑是地上霜。")
    print(search_res)