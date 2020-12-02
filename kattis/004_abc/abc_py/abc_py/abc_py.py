# You will be given three integers A, B and C. 
# The numbers will not be given in that exact order, 
# but we do know that A is less than B and B less than C. 
# In order to make for a more pleasant viewing, we want to 
# rearrange them in a given order.
#
# Input
# The first line contains the three positive integers A, B and C, 
# not necessarily in that order. The three numbers will be less than 
# or equal to 100.
#
# The second line contains three uppercase letters ’A’, ’B’ and ’C’ 
# (with no spaces between them) representing the desired order.
#
# Output
# Output A, B and C in the desired order on a single line, separated by 
# single spaces.
#
# Sample input
# 1 5 3
# ABC
# Sample output
# 1 3 5
#
# Sample input
# 6 4 2
# CAB
# Sample output
# 6 2 4
#
# First we sort the digits, first digit is A, second is B, third is C.
# Then we re-order them to the way requested by the 2nd line:

import sys

inputs = []
for input in sys.stdin:
    inputs.append(input.strip())
numbers = inputs[0]
desired_ordering = inputs[1]

int_array = []
for number in numbers.split():
    int_array.append(int(number))

int_array.sort()

# A=numbers_sorted[0], B=numbers_sorted[1], C=numbers_sorted[2]
output = ''
for digit in desired_ordering:
    digit_num = ord(digit) - ord('A')
    output += str(int_array[digit_num])
    output += ' '

print(output.strip())

