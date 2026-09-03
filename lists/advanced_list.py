# exer1:

# l = [1, 12, 9, 15, 20, 3]

# def list_filter(l):
    

#     return list(filter(lambda x: x >10 , l))

# result = list_filter(l)
# print("The numbers greater than 10 are:", result)


# exercise 2:
from functools import reduce
# from unittest import result


# l = [1, 12, 9, -15, 20, -3]

# def list_filter(l):
#     return list(map(lambda x: x ** 3, filter(lambda x: x < 0 , l)))

# result = list_filter(l)

# print("The numbers less than 0 are:", result)



# l = [1, 12, 9, 15, 20, 3]

# def list_sum(l):
#     return reduce(lambda x, y: x + y, l)

# print("The sum of the numbers is:", list_sum(l))


# xemple d'entrée : [1, 2, 3, 4, 5, 6] avec critère ambda x: x % 2 == 0l → Résultat : ([2, 4, 6], [1, 3, 5]).

# l = [1, 2, 3, 4, 5, 6]

# def list_filter(numbers):
#     even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#     odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
#     result = (even_numbers, odd_numbers)
#     return result



# result = list_filter(l)

# print("The separated numbers are:", result)

# exercice 5:

list1 = [1, 2, 3, 4, 5]
list2 = [6,2,2,3]

def sort_unique(list1, list2):
    combined_list = list1 + list2
    unique_list = list(set(combined_list))
    unique_list.sort()
    return unique_list

result = sort_unique(list1, list2)
print("The unique numbers are:", result)

