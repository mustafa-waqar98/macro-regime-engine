# Lists

spam = ['cat', 'bat']
spam[1] = 'mouse'
print(spam)

# Concatenation and Repetition
A = [1, 2, 3] + ['A', 'B', 'C']
B = ['X', 'Y', 'Z'] * 3

print(A, B)

# For Loops & Lists
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# The in and not in Operators
'howdy' in ['hey', 'hi', 'howdy', 'hello']
'howdy' not in ['hey', 'hi', 'hello']

# Example
my_pets = ['A', 'B', 'C']
print('Enter a pet name: ')
name = input('>')
if name not in my_pets:
    print('I do not have a pet named: ' + name)
else:
    print(name + ' is my pet')

# The Multiple Assignment Trick
cat = ['fat', 'gray', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

# or
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat


# List Item Enumeration
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

# Random Selection & Ordering
import random
pets = ['cats', 'dogs']
random_pet = random.choice(pets)
print(random_pet)

# Magic 8 ball
import random

messages = ['It is certain',
            'It is decidely so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print('Ask a yes or no question:')
input('>')
print(messages[random.randint(0, len(messages) - 1)])