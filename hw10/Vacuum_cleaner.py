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
    max_param = 100
    min_param = 0
    energy_loss = 2
    water_loss = 2

    def __init__(self, battery_charge_level, garbage_fullness, water_left):
        self.battery_charge_level = max(min(float(battery_charge_level), self.max_param), self.min_param)
        self.garbage_fullness = max(min(float(garbage_fullness), self.max_param), self.min_param)
        self.water_left = max(min(float(water_left), self.max_param), self.min_param)

    def wash(self):
        if self.water_left == 0:
            raise NoWater
            # return
        self.water_left = max(self.water_left - self.water_loss, 0)

    def vacuum_cleaner(self):
        self.garbage_fullness = min(self.garbage_fullness + random.randint(1, 3), 100)
        if self.garbage_fullness > 90:
            raise AlmostFilledGarbage
        if self.garbage_fullness == 100:
            print("Container is full")
            input('Press "Enter" to clean container:')
            self.garbage_fullness = 0

    def step_end(self):
        self.battery_charge_level = max(self.battery_charge_level - self.energy_loss, 0)
        if self.battery_charge_level == 0:
            raise NoPower
        elif self.battery_charge_level < 20:
            raise LowPower


def wash(robot):
    # print('wash')
    robot.wash()


def vacuum_cleaner(robot):
    # print('vacuum_cleaner')
    robot.vacuum_cleaner()


test_robot = VacuumRobot(60, 50, 40)


def move(robot):
    i = 5
    k = 0
    while True:
        print("move")
        try:
            wash(robot)
        except NoWater:
            if k == 0:
                print("There is no water, no more washing...")
                k += 1
        try:
            vacuum_cleaner(robot)
        except AlmostFilledGarbage:
            print('Container is almost full, please clear!')
        try:
            robot.step_end()
        except NoPower:
            print("Battery empty, power off")
            break
        except LowPower:
            if i == 0:
                print("The work is stopped! Charge me!")
                break
            else:
                print(f"Battery low, {i} steps remaining")
                i = i - 1
        time.sleep(1)


# move(test_robot)


def simple_move(robot):
    if robot.battery_charge_level > 0:
        print("move")
        try:
            wash(robot)
        except NoWater:
            print("There is no water, no washing...")
        try:
            vacuum_cleaner(robot)
        except AlmostFilledGarbage:
            print('Container is almost full, please clear!')
        try:
            robot.step_end()
        except NoPower:
            print("Battery empty, power off")
        except LowPower:
            print("Battery low, please charge me")
    else:
        print('No power, cant move!')
    time.sleep(1)
