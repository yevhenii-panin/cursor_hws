# task 1
file = open('task1.txt', 'r')
subtitle_data_raw = file.readlines()
file.close()
subtitle_vocab = {}
for i in range(0, len(subtitle_data_raw), 2):
    timecode = subtitle_data_raw[i].replace("\n", "")
    subtitle_text = subtitle_data_raw[i + 1].replace("\n", "")
    subtitle_vocab[timecode] = subtitle_text
print(subtitle_vocab)

# task 2
import pickle

file_with_nums_raw = open('task2', 'rb')
nums = pickle.loads(file_with_nums_raw.read())
file_with_nums_raw.close()
avg_num = sum(nums) / len(nums)
print(avg_num)

# task 3
import openpyxl


class ExcelOpener:
    def __init__(self, name):
        self.file = openpyxl.load_workbook(name)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with ExcelOpener('test_excel.xlsx') as file:
    print(file.active['A1'].value)
    print(file.active['A2'].value)
    print(file.active['A3'].value)
    file.active['B1'].value = 4
    file.active['B2'].value = 5
    file.active['B3'].value = 6
    file.save("test_excel_2.xlsx")
