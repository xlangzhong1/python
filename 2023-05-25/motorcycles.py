motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati" #更改列表元素
print(motorcycles)

#添加元素
motorcycles.append('ducati')
print(motorcycles)

#插入元素
motorcycles.insert(0,'love')
print(motorcycles)

#删除元素
del motorcycles[0]
print(motorcycles)