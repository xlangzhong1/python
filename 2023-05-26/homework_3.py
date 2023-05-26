# for value in range(1,21):
#     print(value)

# numbers = list(range(1,1000001))
# print(numbers)

# numbers = []
# for number in range(1,1000001):
#     numbers.append(number)
# # print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# for value in range(1,21,2):
#     print(value)

# for value in range(3,31,3):
#     print(value)

# numbers = [value ** 3 for value in range(1,11)]
# print(numbers)

numbers = []
for value in range(1,11):
    number = value **3
    numbers.append(number)
print(numbers)

print("The first three items in the list are:")
for number_1 in numbers[0:3]:
    print(number_1)

print("Three items from the middle of the list are")
for number_1 in numbers[4:7]:
    print(number_1)

print("The last three items in the list are")
for number_1 in numbers[-3:]:
    print(number_1)