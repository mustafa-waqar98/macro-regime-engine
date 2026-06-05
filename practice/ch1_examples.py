# This program says hello and asks for my name

print('Hello, world!')
print('What is your name?') # ask for their name
my_name = input('>')
print('It is good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))
print('What is your age?') # As for their age
my_age = input('>')
print('You will be ' + str(int(my_age) + 1) + ' in a year')

# the input() function always returns a string


# The behaviour for rounding half numbers is a bit odd.
print(round(3.5)) # 4
print(round(2.5)) # 2
# For halfway numbers that end with .5, the number is rounded to the nearest even integer. 
# "Banker's Rounding"

