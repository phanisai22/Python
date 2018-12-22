# myList = ["tony","cse", 23]
#
# tuple = "tony", "cse" , 23
# name , section , roll = tuple
# print(name,section,roll)

# dictionary = {
#     "laptop" : 'the device which im using to code python' ,
#     "keyboard" : 'Im definitely not a pro in it .',
#     "wire":' the wire is helping me while ' ,
#     "phone" : 'the device people cannot live without it .',
#     "dress" : "Needed in day to day life"
# }
#
# option = ''
#
# while option != "quit":
#     option= input("enter your option?")
#     if option in dictionary:
#         print(dictionary[option])
#     else :
#         print("the entered option is not found")
#
# description = dictionary.get("mouse","we don't have the key you entered")
# print(description)
#
# sortedItems = sorted(list(dictionary.keys()))
#
# for items in sortedItems:
#     print(items+' : '+dictionary[items])
#
#
# Tuple = dictionary.items()
# print(Tuple,sep='   ')

# myList = ["laptop" , 'phone' , 'mouse' , 'ear bud']
# anotherList = ''
# anotherList += '    '.join(myList)
# print(anotherList)

# -------------------------------------------------------------------------------

# import os
#
# listing = os.walk('.')
#
# for root, directories, files in listing:
#     print(root)
#     for directory in directories:
#         print(directory)
#     for file in files:
#         print(file)

# --------------------------------------------------------------------------------

# OOPs concepts .


class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch(self):
        if not self.on:
            self.on = True
        else:
            self.on = False


ken_wood = Kettle('ken wood', 8.99)
print(ken_wood.make, ken_wood.price)

ken_wood.price = 12.65
print(ken_wood.price)

hamilton = Kettle('hamilton', 14.55)

print('models : {} : {}, {} : {}'.format(ken_wood.make, ken_wood.price,
                                         hamilton.make, hamilton.price))

print('models : {0.make} : {0.price} '.format(ken_wood))

print(hamilton.on)
hamilton.switch()
print(hamilton.on)

Kettle.switch(ken_wood)
print(ken_wood.on)

ken_wood.power = 1.5
# we can create a member like this only for ken_wood instance .
print(ken_wood.power)
# print(hamilton.power)
# this is an error .

print("Kettle switching to atomic :")
Kettle.power_source = 'atomic'

print('ken_wood switching to gas :')
ken_wood.power_source = "gas"

print(Kettle.power_source)
print(ken_wood.power_source)
print('')
#
# print(Kettle.__dict__)
# print(ken_wood.__dict__)
# print(hamilton.__dict__)
