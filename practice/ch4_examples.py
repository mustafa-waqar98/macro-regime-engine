# Functions
# The argument 'Alice' is passed to the parameter 'name' in the function definition.

def say_hello_to(name):
    print('Good morning, ' + name + '!')
    print('Good afternoon, ' + name + '!')
    print('Good evening, ' + name + '!')

say_hello_to('Alice')
say_hello_to('Bob')

# Stacks
def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns') 

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

# Exception Handling
def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# Zigzag
import time, sys
indent = 0
indent_increasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)

        if indent_increasing:
            indent += 1
            if indent == 20:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True

except KeyboardInterrupt:
    sys.exit()