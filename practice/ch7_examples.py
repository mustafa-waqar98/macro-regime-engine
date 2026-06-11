# Dictionaries & Structuring Data

my_cat = {'size': 'fat', 'color': 'gray', 'age': 17}
print(my_cat['size'])

# Comparing Dictionaries and Lists

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'cats', 'moose']
print(spam == bacon) # False

eggs = {'name': 'Mustafa', 'age': '28'}
ham = {'age': '28', 'name': 'Mustafa'}
print(eggs == ham) # True

#Birthdays

birthdays = {'Ahsan': 'Oct 16', 'Ahmad': 'Nov 17'}

while True:
    print('Enter a name: (blank to quit)')
    name = input('>')
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name]+ ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input('>')
        birthdays[name] = bday
        print('Birthday database updated')


spam = {'color': 'red', 'age': 42}

for v in spam.values():
    print(v)
print('')
for k in spam.keys():
    print(k)
print('')
for i in spam.items():
    print(i)


# Checking whether a key exists
picnic_stuff = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnic_stuff.get('cups', 0)) + ' cups')
print('I am bringing ' + str(picnic_stuff.get('eggs', 0)) + ' eggs')

# Nested Dictionaries and Lists
all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandiwches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}
              }

def total_brought(guests,item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought

print('Number of things being brought: ')
print(' - Apples         ' + str(total_brought(all_guests, 'apples')))
print(' - Cups           ' + str(total_brought(all_guests, 'cups')))
print(' - Cakes          ' + str(total_brought(all_guests, 'cakes')))
print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(total_brought(all_guests, 'apple pies')))
