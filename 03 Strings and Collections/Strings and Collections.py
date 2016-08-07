__author__ = 'Graeme Bingham'

# valid strings
x = "It's a good thing"
x = 'This is a test'

# multi line sting
multi = """ this is a
test """

# new line escape
mescape = "this is \n a test"

# escape quotes
test = "This is a \" test"
test = "this is a \' test"

# to display a backslash \
test = "this is a \\ test"

# display as raw string ie displaying paths
path = r'C:\Users\Graeme'

# use string constrctor to cast anything as a string
str(496)

s = 'parrot'
s[4]

# captalize string method
c = 'oslo'
c.capitalize()

d = b'some bytes'
d.split()

# lists
x = []

# add item to end of list
x.append(1.618)

list("characters")

# dict
x = {'bob': '0424220141', 'jess': '94025366'}

# access data through keys
x['jess']

# dicts have no order to them

# for loop on list
cities = ["London", "New York", "Paris", "Oslo", "Helsinki"]
for city in cities:
    print(city)

# for loop on dict
colours = {'crimson': 0xdc143c, 'coral': 0xff7f50, 'teal': 0x008080}
for colour in colours:
    print(colour, colour[colour])

