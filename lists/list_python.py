# # exe1

# list = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

# new_list = []

# for i in list:
#     average = sum(list) / len(list)
#     if i > average:
#         new_list.append(i)

# print(f"The average of the list is:", average)
# print("The numbers greater than the average are:", new_list)        

# exer2:

# word1 = "Le langage Python est très populaire" 
# word2 = "Python est un langage puissant"

# new_word = []

# for i in word1.split():
#     if i in word2.split() and i not in new_word:
#         new_word.append(i)

# print("The characters that are present in both strings are:", new_word)   
# 

# exer3:
# stock = ["Stylo", 25, "Classeur", 100, "Crayon", 12, "Surligneur", 40, "Feutre", 5]   
# str_list = []
# num_list = []
# for i  in stock:
#     if isinstance(i, str):
#         str_list.append(i)
#     else:
#         num_list.append(i)    

# def sort_list(list):
#     str_list.sort()
#     num_list.sort()
#     return str_list, num_list

# result = sort_list(str_list)
# print("The sorted list of strings is:", result[0])  
# print("**************")
# print("The sorted list of numbers is:", result[1])      

# exercise 4:
# Fruits = ["pomme", "banane", "orange", "kiwi", "mangue"]

# def searchElement(ele,list):
#     for i in list:
#         if i == ele:
#             return True
#     return False

# result = searchElement("orange",Fruits)
# print(result)    

# exercise 5:
# L = [7 , 23 , 5 , 23 , 7 , 19 , 23 , 12 , 29]
# count = 0

# def searchElement(ele,list):
#     for i in list:
#         if i == ele:
#             global count
#             count += 1
#     return count

# result = searchElement(23,L)
# print(result)


notes_eleves = { "Amine": 15.5, "Yassine": 19.0, "Reda": 14.2, "Malak": 8.7, "Manal": 20.0, "Ahmed": 7.5,"Saad": 11.3, "Hannae": 9.8 }
# seperated the students into two lists based on their grades: those who passed (grade >= 10) and those who failed (grade < 10).
passed = {k: v for k, v in notes_eleves.items() if v >= 10}
failed = {k: v for k, v in notes_eleves.items() if v < 10}

notes_eleves = {"passed": passed, "failed": failed}
print(notes_eleves)