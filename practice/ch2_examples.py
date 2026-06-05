

True and True       # True
True and False      # False
False and True      # False
False and False     # False

True or True       # True
True or False      # True
False or True      # True
False or False     # False

not True           # False
not False          # True
not not True       # True
not not False      # False

# Blocks of Code
# Python expects a new block immediately after a colon (:)

username = 'Mustafa'
password = 'password123'
if username == 'Mustafa':
    print('Hello,', username)
    if password == 'password123':
        print('Access granted')
    else:
        print('Acess denied')   

# Opposite Day
today_is_opposite_day = True

# Set say_it_os_opposite_day based on today_is_opposite_day
if today_is_opposite_day == True:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False

# If it is opposite day, toggle say_it_is_opposite_day
if today_is_opposite_day == True:
    say_it_is_opposite_day = not say_it_is_opposite_day

# Say what day it is
if say_it_is_opposite_day == True:
    print('Today is opposite day')
else:
    print('Today is not opposite day')


# Dishonest Capacity Calculator
print('Enter TB or GB for the advertised unit:')
unit = input('>')

# Calculate the amount that the advertised capacity lies:
if unit == 'TB' or unit == 'tb':
    discrepancy = 1000**4 / 1024**4
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000**3 / 1024**3

print('Enter the advertised capacity:')
advertised_capacity = float(input('>'))

# Calculate the real capacity, round it to the nearest hundredths,
# and convert it to a string so it can be concatenated:
real_capacity = str(round(advertised_capacity * discrepancy, 2))

print('The real capacity is ' + real_capacity + ' ' + unit)