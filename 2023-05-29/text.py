# Text 6-1
# alice = {'first_name':'alice',
#          'last_name':'loder',
#          'age':'19',
#          'city':'LA'}

# print(alice['first_name'])
# print(alice['last_name'])
# print(alice['age'])
# print(alice['city'])

#Text 6-7
people = []

alice = {'first_name':'alice',
         'last_name':'loder',
         'age':'19',
         'city':'LA'}

bob = {
    'first_name': 'bob',
    'last_name': 'smith',
    'age': '25',
    'city': 'New York'
}

charlie = {
    'first_name': 'charlie',
    'last_name': 'brown',
    'age': '30',
    'city': 'Chicago'
}

people = [alice, bob, charlie]

for person in people:
    print("\nFirst Name:", person['first_name'])
    print("Last Name:", person['last_name'])
    print("Age:", person['age'])
    print("City:", person['city'])