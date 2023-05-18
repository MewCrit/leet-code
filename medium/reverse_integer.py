# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
 

# Example 1:

# Input: x = 123
# Output: 321

# Example 2:

# Input: x = -123
# Output: -321

# Example 3:

# Input: x = 120
# Output: 21


x = 123

result = 0

is_negative = x < 0
if is_negative:
    x = abs(x)
    
reversed_num = int(str(x)[::-1])

if reversed_num > 2**31 - 1:
    result = 0

result = -reversed_num if is_negative else reversed_num

print(result)



