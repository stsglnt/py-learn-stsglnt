import functools
import operator

my_original_list = [1, 2, 3, 4, 5, 6, 7, 9]

my_comprehension_list = [a - 5 for a in my_original_list if a > 5]
my_filter_list = list(filter(lambda a: a > 5, my_original_list))
my_mapped_list = list(map(lambda a: a*2, my_original_list))
my_reduced_list = functools.reduce(lambda a, b: a+b, my_original_list)
my_reduced_simplified_list = functools.reduce(operator.add, my_original_list)


print(f"{my_comprehension_list=}")
print(f"{my_filter_list=}")
print(f"{my_mapped_list=}")
print(f"{my_reduced_list=}")
print(f"{my_reduced_simplified_list=}")

