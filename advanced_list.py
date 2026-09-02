# exer1:

# l = [1, 12, 9, 15, 20, 3]

# def list_filter(l):
    

#     return list(filter(lambda x: x >10 , l))

# result = list_filter(l)
# print("The numbers greater than 10 are:", result)


# exercise 2:
from unittest import result


l = [1, 12, 9, -15, 20, -3]

def list_filter(l):
    return list(map(lambda x: x ** 3, filter(lambda x: x < 0 , l)))

result = list_filter(l)

print("The numbers less than 0 are:", result)