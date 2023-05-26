#3-4 创建一个邀请名单
people = ['bob','alice','john']
message = "Hello " + people[0].title() + ", " + people[1].title() + " and " + people[2].title() + ", I want to invite all of you to come to my dinner"
print(message)

#3-5 某人因故无法来参加，print message
message = "I'm so sorry that " + people[-1].title() + " cannot come because something"
print(message)

people[-1] = "judy"
print(people)
message = "Hello " + people[0].title() + ", " + people[1].title() + " and " + people[2].title() + ", I want to invite all of you to come to my dinner"
print(message)

#3-6 添加嘉宾
print("I just found a bigger table, so we can invite more people to enjoy dinner")
people.insert(0,"wendy")
print(people)
people.insert(2,"charlie")
print(people)
people.append("lily")
print(people)
message = "Hello " + people[0].title() + ", " + people[1].title() + ", "  + people[2].title() + ", " + people[3].title() + ", " + people[4].title()  + " and " + people[5].title() + ", I want to invite all of you to come to my dinner"
print(message)

#3-7 缩减名单
print("I'm so sorry that i can only invite two persons cause the table can't be deliver in time ")
popped_people_1 = people.pop(0)
print("I'm so sorry that i can't invite you to my dinner, " + popped_people_1.title())
print(len(people))
popped_people_2 = people.pop(0)
print("I'm so sorry that i can't invite you to my dinner, " + popped_people_2.title())
popped_people_3 = people.pop(0)
print("I'm so sorry that i can't invite you to my dinner, " + popped_people_3.title())
popped_people_4 = people.pop(0)
print("I'm so sorry that i can't invite you to my dinner, " + popped_people_4.title())
print(people) #直至只有两位嘉宾
print(len(people))

message = "Hello " + people[0].title() +  ", I want to invite all of you to come to my dinner"
print(message)
message = "Hello " + people[1].title() +  ", I want to invite all of you to come to my dinner"
print(message)

del people[0]  #del 语句的使用
print(people)

del people[0]
print(people) #作业完成