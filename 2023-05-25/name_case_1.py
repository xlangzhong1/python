name = "eric"
message = "Hello" + " " + name + "," + "would you like learn some Python today?"
print(message)

#名字大小写
name = "eric"
print(name.title())
print(name.upper())
print(name.lower())

#名言1
first_name = "albert"
last_name = "einsterin"
full_name = first_name + " " + last_name
message = full_name.title() + " " + 'once said, "A person who never made a mistake never tried anything new"'

print(message)

#strip用法
first_name = "\talbert"
last_name = "einsterin\n "
full_name = first_name + " " + last_name

print(full_name)
print(full_name.lstrip())
print(full_name.rstrip())
print(full_name.strip())


