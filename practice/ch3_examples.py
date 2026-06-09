spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

print('')


#While loops
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

print('')

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input('>')
print('Thank you!')

#break statement example
while True:
    print('Please type your name.')
    name = input('>')
    if name == 'your name':
        break
print('Thank you!')

#continue statement example
while True:
    print('Who are you?')
    name = input('>')
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password?')
    password = input('>')
    if password == 'swordfish':
        break
print('Access granted.')

#for loop statement and the range() function
print('Hello!')
for i in range(5):
    print('On this iteration, i is set to ' + str(i))
print('Goodbye!')

#same example as above but with a while loop
print('Hello!')
i = 0
while i < 5:
    print('On this iteration, i is set to ' + str(i))
    i = i + 1
print('Goodbye!')  

total = 0
for num in range(101):
    total = total + num
print(total)

'''import sys
while True:
    print('Type exit to exit.')
    response = input('>')
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
'''

# Guess the number
import random
secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for guesses_taken in range(1,7):
    print('Take a guess.')
    guess = int(input('>'))

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break

if guess == secret_number:
    print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
else:    
    print('Nope. The number I was thinking of was ' + str(secret_number) + '.')
