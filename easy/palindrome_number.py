# Given an integer x, return true if x is a palindrome, and false otherwise.

num = -121
char_array = list(str(num))
reversed  = char_array.reverse()

reversed_string  = ''.join(char_array)

palin = str(reversed_string)

if palin == str(num):
    print(f'{num} is a palindrome')
else:
    print(f'{num} is not a palindrome')

