# def welcome():
# 	print("Welcome to the Hundred Acre Wood!")
# welcome()

# def greeting(name):
#     print(f"Welcome to The Hundred Acre Wood ${name}! My name is Christopher Robin")
# greeting("Michael")
# greeting("Winnie the Pooh")        


def get_item(items, x):
    if x > len(items)-1:
        return print(None)
    return print(items[2])

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)
