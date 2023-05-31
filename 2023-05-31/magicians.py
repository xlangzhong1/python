#8-9
def show_magicians(magician_list):
    for magician in magician_list:
        print("\n" + magician.title())

def make_great(magician_list):
    new_magician_list = []
    for magician in magician_list:
        new_magician = "the Great " + magician
        new_magician_list.append(new_magician)
    return new_magician_list



magicians = ['bob', 'sarah', 'lily']
show_magicians(magicians)

new_magicians = make_great(magicians)
show_magicians(new_magicians)
