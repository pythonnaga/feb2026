# 1
my_list = [10, 20, 30, 40, 50, 11]
my_list.reverse()
print(my_list)


# 2
empty_list = []
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

for num in list1:
    if num in list2:
        empty_list.append(num)

print(empty_list)


# 3
original_list = [1, 2, 2, 3, 4, 4, 5]
empty_list = []

for num in original_list:
    if num not in empty_list:
        empty_list.append(num)

print(empty_list)


# 4
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
empty_list = []

for number in duplicated_list:
    if number not in empty_list:
        empty_list.append(number)

print(empty_list)


# 5
num_1 = [1, 2, 3.7, 5]
num_2 = ["bhanu", 5, 2]
print(num_1 + num_2)


# 6
num = [5, 1, 3, 4]
print(num * 5)


# 7
number = [1,2,3,4,5,6,7,8,9,10]
result = number[1::2]
print(result)


# 8
number = [1,2,3,5]
result = [10,11,12] + number
print(result)


# 9
numbers = [1,2,3,4,5,6,7,8,9,10]
print([i**2 for i in numbers])
print([i % 2 == 0 for i in numbers])


words = ["apple", "banana", "cherry", "date"]
length = [len(word) for word in words]
print(length)