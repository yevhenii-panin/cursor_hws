# Task 1
# Напишіть калькулятор в якого будуть реалізовані операції додавання, віднімання, множення, ділення, піднесення в степінь,
# взяття з під кореня, пошук відсотку від числа
#
# Огорніть в конструкцію try... except... потенційно "небезпечні" місця, наприклад отримання числа і приведення до типу даних
# або інструкції математичних операцій
#
# заповніть ваш скрипт логами
# Логи здебільшого інформаційні (викликали таку функцію з такими аргументами)
# + логи з помилками
# причому логи повинні записуватись у файл, тому що в консолі ви будете взаємодіяти з калькулятором,
# лог файл завжди відкриваєтсья в режимі дозапису.
# так як ви працюєте з файлом не забудьте про те що це потенційне місце поломки
import logging

try:
    file = open("hw9_task1.log", 'r')
except:
    file = open("hw9_task1.log", 'w')
finally:
    file.close()

log_template = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, filename="hw9_task1.log", filemode="a", format=log_template)


def sum_func():
    print('-sum-')
    logging.info("calling sum_func")
    str_a = input('first num:')
    try:
        a = int(str_a)
    except ValueError:
        print('a is not decimal')
        logging.error('not decimal first number to sum')
        return
    str_b = input('second num:')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to sum')
        return
    c = a + b
    print(f"{a} + {b} = {c}")
    logging.info(f"sum_func is successfully finished, {a}, {b}")
    return c


def rem_func():
    print('-rem-')
    logging.info("calling rem_func")
    str_a = input('first num:')
    try:
        a = int(str_a)
    except ValueError:
        print('a is not decimal')
        logging.error('not decimal first number to rem')
        return
    str_b = input('second num:')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to rem')
        return
    c = a - b
    print(f"{a} - {b} = {c}")
    logging.info(f"rem_func is successfully finished, {a}, {b}")
    return c


def mul_func():
    print('-mul-')
    logging.info("calling mul_func")
    str_a = input('first num:')
    try:
        a = int(str_a)
    except ValueError:
        print('a is not decimal')
        logging.error('not decimal first number to mul')
        return
    str_b = input('second num:')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to mul')
        return
    c = a * b
    print(f"{a} * {b} = {c}")
    logging.info(f"mul_func is successfully finished, {a}, {b}")
    return c


def div_func():
    print('-div-')
    logging.info("calling div_func")
    str_a = input('first num:')
    try:
        a = int(str_a)
    except ValueError:
        print("a is not decimal")
        logging.error('not decimal first number to div')
        return
    str_b = input('second num:')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to div')
        return
    try:
        c = a / b
        print(f"{a} / {b} = {c}")
        logging.info(f"div_func is successfully finished, {a}, {b}")
        return c
    except ZeroDivisionError:
        print("b is 0, ZeroDivisionError")
        logging.error('trying to divide by zero')
        return


def deg_func():
    print('-deg-')
    logging.info("calling deg_func")
    str_a = input('first num:')
    try:
        a = int(str_a)
    except ValueError:
        print("a is not decimal")
        logging.error('not decimal first number to deg')
        return
    str_b = input('second num:')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to deg')
        return
    try:
        c = a ** b
    except ZeroDivisionError:
        print("0 ^ -1 can't be compute")
        logging.error('trying 0 ^ -1')
        return
    print(f"{a} ^ {b} = {c}")
    logging.info(f"deg_func is successfully finished, {a}, {b}")
    return c


def root_func():
    print('-root-')
    logging.info("calling root_func")
    str_a = input('first num:')
    try:
        a = int(str_a)
    except ValueError:
        print("a is not decimal")
        logging.error('not decimal first number to root')
        return
    str_b = input('second num:')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to root')
        return
    try:
        c = a ** (1 / b)
        print(f"{a} ^ {b} = {c}")
        logging.info(f"deg_func is successfully finished, {a}, {b}")
        return c
    except ZeroDivisionError:
        print("b is 0, can't get root, ZeroDivisionError")
        logging.error('trying to divide by zero (in degree)')
        return


def per_func():
    print('-per-')
    logging.info("calling per_func")
    str_a = input('first num:')
    try:
        a = int(str_a)
    except ValueError:
        print("a is not decimal")
        logging.error('not decimal first number to per')
        return
    str_b = input('second num:')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to per')
        return
    c = a * b / 100
    print(f"{b}% from {a} = {c}")
    logging.info(f"per_func is successfully finished, {a}, {b}")
    return c


sum_func()
rem_func()
mul_func()
div_func()
deg_func()
root_func()
per_func()

# Task 2
# Напишіть клас робота пилососа
# в ініт приймається заряд батареї, заповненість сміттєбака і кількість води
#
# реалізуйте функцію move() - нескінченний цикл який на кожній ітерації "замерзає" на 1 сек
# окрім цього на кожній ітерації викликаються функції "wash" і "vacuum cleaner"
# (в цих функціях повинні стояти прніти "wash" і "vacuum cleaner" відповідно),
# також на кожній ітерації прінтиться "move"
# + на кожній ітерації цикла заряд батареї і кількість води зменшується на певну кількість
# (задайте в статік аргументах класу як конфіг пилососа, або в окремому конфіг файлі),
# а кількість сміття збільшується
#
# Напишіть власні ексепшини які кидаються коли заряд батареї менше ніж 20%, заряд батареї 0%, кількість води - 0, кількість сміття більша ніж певне число
# опрацюйте ваші ексепшини (наприклад якщо заряд батареї менше 20% то цикл робить ще певну кількість ітерацій і зупиняється,
# якщо вода закінчилась то пилосос тепер не миє підлогу а тільки пилососить,
# 0 відсотків заряду - пилосос кричить щоб його занесли на зарядку бо сам доїхати не може)
import time
import random


class LowPower(Exception):
    pass


class NoPower(Exception):
    pass


class NoWater(Exception):
    pass


class AlmostFilledGarbage(Exception):
    pass


class VacuumRobot:
    energy_loss = 2
    water_loss = 2

    def __init__(self, battery_charge_level, garbage_fullness, water_left):
        self.battery_charge_level = battery_charge_level
        self.garbage_fullness = garbage_fullness
        self.water_left = water_left

    def wash(self):
        if self.water_left == 0:
            raise NoWater
            return
        self.water_left = max(self.water_left - self.water_loss, 0)

    def vacuum_cleaner(self):
        self.garbage_fullness = min(self.garbage_fullness + random.randint(1, 3), 100)
        if self.garbage_fullness > 90:
            raise AlmostFilledGarbage

    def step_end(self):
        self.battery_charge_level = max(self.battery_charge_level - self.energy_loss, 0)
        if self.battery_charge_level == 0:
            raise NoPower
        elif self.battery_charge_level < 20:
            raise LowPower


def wash(robot):
    print('wash')
    robot.wash


def vacuum_cleaner(robot):
    print('vacuum_cleaner')
    robot.vacuum_cleaner


test_robot = VacuumRobot(60, 50, 40)


def move(robot):
    i = 5
    while True:
        print("move")
        wash(robot)
        try:
            vacuum_cleaner(robot)
        except AlmostFilledGarbage:
            print('Container is almost full, please clear!')
        try:
            robot.step_end
        except NoPower:
            print("Battery empty, power off")
            break
        except LowPower:
            print(f"Battery low, {i} steps remaining")
            i = i - 1
            if i == 0:
                break
        time.sleep(1)


move(test_robot)
