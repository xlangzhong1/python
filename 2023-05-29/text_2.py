#7-1
# message = input("What type of car are you looking to rent: ")
# print("Let me see if I can find you a " + message.title())

#7-3
# number = input("Text a number: ")
# number = int(number)

# if number % 10 == 0:
#     print(str(number) + " is a multiple of 10.")
# else:
#     print(str(number) + " is not a multiple of 10.")

#7-6
active = True
while active:
    promt = input("\nHow old are you ?")
    if promt == "quit":
        break
    promt = int(promt)
    if promt == 3:
        print("your tickt cost nothing!")
    elif promt >= 3 and promt <= 12:
        print("your tickt cost 10$!")
    elif promt > 12:
        print("your tickt cost 15$!")
    else:
        break
