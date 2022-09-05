import json
import csv

def poetry_data_process():
    result_list = []
    for i in range(1, 73282):
        if i % 1000 == 0:
            print("loading json", i)
        file_name = ".\data\poetry\poetry_" + str(i) + ".json"
        try:
            with open(file_name, mode='r', encoding='utf-8') as f:
                data = json.load(f)
                content = data["content"]
                translation = data["fanyi"]
                content_lines = content.split("\n")
                translation_lines = translation.split("\n")
                if translation_lines[0] == "注释":
                    continue
                for idx in range(len(content_lines)):
                    if translation_lines[idx+1] == "注释":
                        break
                    if len(content_lines[idx]) >= 50 or len(translation_lines[idx+1]) >= 100:
                        continue
                    if content_lines[idx] != "" and translation_lines[idx+1] != "" and translation_lines[idx+1][0] != '(':
                        result_list.append([content_lines[idx], translation_lines[idx+1]])
                # print(file_name)
        except:
            pass
    with open('output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(result_list)

if __name__ == "__main__":
    poetry_data_process()