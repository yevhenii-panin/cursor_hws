# 1. Write the method that return the number of threads currently in execution.
# Also prepare the method that will be executed with threads and run during the first method counting.
from threading import Thread, active_count
import time
import random


def kind_a_working():
    time.sleep(random.randint(1, 3))


def count_threads():
    print(active_count())


if __name__ == '__main__':
    threads = [Thread(target=kind_a_working) for _ in range(5)]
    for thread in threads:
        thread.start()
    count_threads()
    for thread in threads:
        thread.join()

# 2. Print current date by using 2 threads.
# #1. Define a subclass using Thread class.
# #2. Instantiate the subclass and trigger the thread.
from threading import Thread
import datetime


class NewThreadClass(Thread):
    def run(self) -> None:
        print(f"Thread - {self.name}. Date is {datetime.date.today()}")


thread_1 = NewThreadClass()
thread_2 = NewThreadClass()

thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()


# 3. Use Pool.apply() to get the row wise common items in list_a and list_b.
# list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
# list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]

# 3. Use Pool.apply() to get the row wise common items in list_a and list_b.
# list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
# list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
from multiprocessing import Pool


def common_items(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    return list(set_1.intersection(set_2))


if __name__ == '__main__':
    list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
    list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
    with Pool(5) as pool:
        result = [pool.apply(common_items, args=(list_a[i], list_b[i])) for i in range(len(list_a))]
        print(result)

# 4. Divide the work between 2 methods: print_cube that returns the cube of number and
# print_square that returns the square of number. These two methods should be executed by using 2 different processes.
from multiprocessing import current_process, Process


def print_cube(n):
    print(f'Cube of {n} is {n ** 3}, process is {current_process().name}')
    return n ** 3


def print_square(n):
    print(f'Square of {n} is {n ** 2}, process is {current_process().name}')
    return n ** 2


if __name__ == '__main__':
    i = int(input("Your Number: "))
    process1 = Process(target=print_cube, args=(i,))
    process2 = Process(target=print_square, args=(i,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
