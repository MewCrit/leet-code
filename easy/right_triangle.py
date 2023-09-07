# Print a right triangle according to the integer input
# Example : input 7 
# Expected 
# *
# **
# ***
# ****
# *****
# ******
# *******

num = 7
str_arr = ''

for c in range(num):
   star = '*'
   str_arr +=star
   print(str_arr)
str_arr = ''
