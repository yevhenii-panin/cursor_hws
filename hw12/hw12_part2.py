# coding=utf8
"""
2. Create a script with arguments:

source_file_path; required: true;
start_salary; required: false; help: starting point of salary;
end_salary; required: false; help: the max point of salary;
position; required: false; help: position role
age; required: false; help: Age of person
language; required: false; help; Programming language

Based on this info generate a new report of average salary.
"""
import csv
import argparse

parser = argparse.ArgumentParser(description="The script should generate personal salary report")

parser.add_argument("--source_file_path", required=True)
parser.add_argument("--start_salary", required=False, help="starting point of salary")
parser.add_argument("--end_salary", required=False, help="the max point of salary")
parser.add_argument("--position", required=False, help="position role")
parser.add_argument("--age", required=False, help="Age of person")
parser.add_argument("--language", required=False, help="Programming language")
args = parser.parse_args()
if args.start_salary is None:
    args.start_salary = int(0)
else:
    args.start_salary = int(args.start_salary)
if args.end_salary is None:
    args.end_salary = int(18000)
else:
    args.end_salary = int(args.end_salary)
# if args.age is not None:
#     args.age = int(args.age)

lst_salary = []
i = 0
with open(f'{args.source_file_path}/2020_june_mini.csv', "r", encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        if i == 0:
            i = 1
            continue
        if int(row[2]) >= args.start_salary:
            if int(row[2]) <= args.end_salary:
                if args.position is None:
                    if args.age is None:
                        if args.language is None:
                            lst_salary.append(int(row[2]))
                        else:
                            if args.language == row[7]:
                                lst_salary.append(int(row[2]))
                    else:
                        if args.age == row[9]:
                            if args.language is None:
                                lst_salary.append(int(row[2]))
                            else:
                                if args.language == row[7]:
                                    lst_salary.append(int(row[2]))
                else:
                    if args.position == row[4]:
                        if args.age is None:
                            if args.language is None:
                                lst_salary.append(int(row[2]))
                            else:
                                if args.language == row[7]:
                                    lst_salary.append(int(row[2]))
                        else:
                            if args.age == row[9]:
                                if args.language is None:
                                    lst_salary.append(int(row[2]))
                                else:
                                    if args.language == row[7]:
                                        lst_salary.append(int(row[2]))

if len(lst_salary) > 0:
    print(f"Average salary for your request is {sum(lst_salary) / len(lst_salary)}")
else:
    print("There is no data for your request!")
# --source_file_path . --age 30