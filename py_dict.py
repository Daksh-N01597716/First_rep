# simple_dict.py
my_dict = {'apple': 'red'}

def add_fruit(fruit, color):
    my_dict[fruit] = color
    print(f"Added {fruit}: {color}")
    print("Current dictionary:", my_dict)

add_fruit('banana', 'yellow')
add_fruit('grape', 'purple')  # New fruit added
add_fruit('cherry', 'red')  # New fruit added
