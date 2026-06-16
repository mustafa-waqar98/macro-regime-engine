# Strings & Text Editing

print("M \t W")
print("M \n W")

# Raw strings
print(r'The file is in C:\Users\Mustafa')
# a raw string makes it easier to enter string values that have blackslashes by ignoring all escape sequences

# Multiline Strings
# Any quotes, tabs, or newlines in betweem "triple quotes" are considered part of the string

print('''Dear Alice,
      
      Can you feed Eve's cat this weekend?

      Sincerely, 
      Bob
      ''')

# Indexes and Slices
greeting = 'Hello, world!'
print(greeting[0])          # "H"
print(greeting[4])          # "o"
print(greeting[-1])         # "!"
print(greeting[0:5])        # "Hello"
print(greeting[:5])         # "Hello"
print(greeting[7:-1])       # "world"
print(greeting[7:])         # "world"

# Useful String Methods
spam = 'Hello, world!'
print(spam.upper())
print(spam.lower())

# .islower() ans .isupper() return a Boolean True or False
# .isalpha() returns True if the string consists only of letters and isn't blank
# .isalnum() returns True if the string consists only of letters and numbers (alphanumerics) and isn't blank
# .isdeimal() returns True if the string consists only of numeric character and isn't blank
# .isspace() returns True if the string consists only of spaces, tabs, and newlines and isn't blank
# istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
# .startswith() and endswith() methods return True if the string value on which they're called begins or ends (respectively) with the string passed to the method

# Joining and Splititng Strings

# .join() method is useful when you have a list of strings that need to be joined together into a single string value
', '.join(['cats', 'dogs', 'bats'])
# 'cats, dogs, bats'
' '.join(['My', 'name', 'is', 'Mustafa'])
# My name is Mustafa

# a common use of .split() is to split a multline string along the newline characters
spam = '''Dear Alice
There is a milk bottle in the fridge
that is labeled "Milk Experiment"'''
# ['Dear Alice', 'There is a milk bottle in the fridge', 'that is labeled "Milk Experiment"]


# Justifying & Centering Text
# .rjust() and .ljust() return a padded version of the string
# .center() centers the text

# Removing Whitespace
# .strip() will return a new string without any whitespace characters at the beginning or end
# .lstrip() and .rstrip() remove remove whitespace characters from either end

# Numeric Code Points of Characters
# ord() function gets the code point of one-character string
# chr() function gets the one-character string of an integer code point