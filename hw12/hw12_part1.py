"""
In the homework directory you can find the directory arg_parser_homework where you can find 2020_june_mini.csv file.

1. Create a script with arguments:

exp; required: false; default: min(exp)
current_job_exp; required: false; default: max(current_job_exp)
sex; required: false
city; required: false
position; required: false
age; required: false
path_to_source_files; required: true;
destination_path; required: false; default: .
destination_filename; required: false; default: f"2020_june_mini.csv".
The script should read the .csv file and get the information based on your input and generate a new .csv
file with that info

Example of input:
-exp 3 -sex female -position DevOps -city Kyiv --path_to_source_files . ...
"""
# import csv
# import codecs
# exp = []
# current_job_exp = []
# i = 1
# with codecs.open('2020_june_mini.csv', encoding="utf8", errors='replace') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         try:
#             exp.append(int(row[5]))
#             current_job_exp.append(int(row[6]))
#         except ValueError:
#             continue
# print(min(exp)) # 0
# print(max(current_job_exp)) # 10

import argparse
import csv

parser = argparse.ArgumentParser(
    description='The script should read the .csv file and get the information based on your input and generate a new .csv file with that info')
parser.add_argument("--exp", required=False, default=0, help="Experience")
parser.add_argument("--current_job_exp", required=False, default=10, help="Experience on current job")
parser.add_argument("--sex", "-s", required=False, help="Sex")
parser.add_argument("--city", required=False, help="City")
parser.add_argument("--position", "-p", required=False, help="Position")
parser.add_argument("--age", "-a", required=False, help="Age")
parser.add_argument("--path_to_source_files", required=True, help="Path to source file")
parser.add_argument("--destination_path", required=False, default=".", help="Path for new file")
parser.add_argument("--destination_filename", required=False, default="2020_june_mini_new.csv", help="Name of new file")
args = parser.parse_args()

i = 0
path_to_open = f'{args.path_to_source_files}/2020_june_mini.csv'
path_to_create = f'{args.destination_path}/{args.destination_filename}'
with open(path_to_open, 'r', encoding="utf8") as file:
    with open(path_to_create, 'w', encoding="utf8") as new_file:
        reader = csv.reader(file)
        for row in reader:
            if i == 0:
                new_file.write(f"{str(row)[1:len(str(row)) - 1]}\n")
                i = 1
                continue
            if args.age is None or args.age == row[9]:
                if args.city is None or args.city == row[1]:
                    if args.position is None or args.position == row[4]:
                        if args.sex is None or args.sex == row[10]:
                            if args.exp == row[5]:
                                if args.current_job_exp == row[6]:
                                    new_file.write(f"{str(row)[1:len(str(row)) - 1]}\n")

print("Your file is ready!, 2020_june_mini_new.csv")
# --path_to_source_files . --age 30 --current_job_exp 3 --exp 3
