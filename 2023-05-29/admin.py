#Text 5-8
# users = ['admin','admi','hym','mkx','sdw']

# for user in users:
#     if user == 'admin':
#         print("Hello " + user + ", would you like to see a a status report?")
#     else:
#         print("Hello " + user.title() + ", thank you for logging in again.")

#Text 5-9
# users = []

# if users:
#     for user in users:
#         if user == 'admin':
#             print("Hello " + user + ", would you like to see a a status report?")
#         else:
#             print("Hello " + user.title() + ", thank you for logging in again.")
# else:
#     print("We need to find some users!")

#Text 5-10
# current_users = ['John','admi','hym','mkx','sdw']
# new_users = ['john','mkx','charlie','wendy','admi']
# current_users_lower = []

# for current_user in current_users:
#     current_users_lower.append(current_user.lower())

# for new_user in new_users:
#     if new_user.lower() in current_users_lower:
#         print("The name: " + new_user + " has been used. Plese input another one")
#     else:
#         print("You can use the name: " + new_user)


#Text 5-10 哥哥写的
# current_users = ['John','admi','hym','mkx','sdw']
# new_users = ['john','mkx','charlie','wendy','admi']
# flag = True
# for new_user in new_users:
#     for current_user in current_users:
#         if new_user.lower() == current_user.lower():
#             print("The name: " + new_user + " has been used. Plese input another one")
#             flag = False
#             break
#     if flag:
#         print("You can use the name: " + new_user)
#     flag = True

#Text 5-11
numbers = [value for value in range(1,101)]
print(numbers)

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")



