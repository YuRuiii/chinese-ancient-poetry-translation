import json
import csv

def poetry_data_process():
    result_list = []
    for i in range(1, 73282):
        if i % 100 == 0:
            print("loading json", i)
        file_name = ".\data\poetry\poetry_" + str(i) + ".json"
        try:
            with open(file_name, mode='r', encoding='utf-8') as f:
                data = json.load(f)
                content = data["content"]
                translation = data["fanyi"]
                content_lines = content.split("\n")
                translation_lines = translation.split("\n")
                for idx in range(len(content_lines)):
                    if content_lines[idx] != "" and translation_lines[idx+1] != "":
                        result_list.append([content_lines[idx], translation_lines[idx+1]])
                # print(file_name)
        except:
            pass
    with open('output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(result_list)

if __name__ == "__main__":
    poetry_data_process()