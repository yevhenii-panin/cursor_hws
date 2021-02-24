int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

lst_d.append(4)
lst_d.append(5)
print(id(lst_d))

print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

print("Anna has {} apples and {} peaches".format(1, 2))
print("Anna has {1} apples and {0} peaches".format(1, 2))
print("Anna has {0:4} apples and {1:2} peaches".format(1, 2))

first = "1"
second = "2"
print(f"Anna has {first} apples and {second} peaches")
print("Anna has %s apples and %s peaches" % (1, 2))

dict_subst = {"first": "1", "second": "2"}
print("Anna has %(first)s apples and %(second)s peaches" % dict_subst)

# lst = []
# for num in range(10):
#    if num % 2 == 1:
#        lst.append(num ** 2)
#    else:
#        lst.append(num ** 4)
# print(lst)

lst_comp_1 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_comp_1)

# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
# print(list_comprehension)

lst_comp_2 = []
for num in range(10):
    if num % 2 == 0:
        lst_comp_2.append(num // 2)
    else:
        lst_comp_2.append(num * 10)
print(lst_comp_2)

# d = {}
# for num in range(1, 11):
#    if num % 2 == 1:
#         d[num] = num ** 2
# print(d)

dict_comp3 = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_comp3)

# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)

dict_comp4 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_comp4)

# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
# print(dict_comprehension)

dict5 = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        dict5[num] = num ** 3
print(dict5)

# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
# print(dict_comprehension)

dict6 = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        dict6[num] = num ** 3
    else:
        dict6[num] = num
print(dict6)

# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y

foo = lambda x, y: min(x, y)


# foo = lambda x, y, z: z if y < x and x > z else y

def foo(x, y, z):
    if y < x & x > z:
        return z
    else:
        return y


lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
print(sorted(lst_to_sort, reverse=True))
lst_to_sort_new = list(map(lambda x: x*2, lst_to_sort))
print(lst_to_sort_new)

from operator import add

list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_C1 = list(map(lambda a, b: a+b, list_A, list_B))
print(list_C1)
list_C1 = list(map(lambda a, b: a**b, list_A, list_B))
print(list_C2)

from functools import reduce

sum_lst = reduce(lambda a, b: a + b, lst_to_sort)
print(sum_lst)

lst_to_sort_new2 = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(lst_to_sort_new2)

b = range(-10, 10)
b_new = list(filter(lambda x : (x<0), b))
print(b_new)

list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
print(list(filter(lambda x: x in list_1, list_2)))
