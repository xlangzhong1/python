cars = ['bmw','audi','toyota','subaru']
print(cars)

#方法 “sort” 的使用
# cars.sort()
# print(cars)
#或者可以使用参数“reverse=True”
# cars.sort(reverse=True)
# print(cars)

#使用函数sorted 对列表进行临时徘序
# print("Here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)

#方法 “reverse” 的使用 ， 效果是永久的倒排
cars.reverse()
print(cars)