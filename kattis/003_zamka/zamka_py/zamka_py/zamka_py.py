# https://open.kattis.com/problems/zamka
# The impossible has happened. Bear G. has fallen into his own trap. 
# Lured by a delicious box of Domaćica, without even thinking, he rushed 
# and fell into his trap. In order to get out of the trap, he must solve 
# the following task with your help. You are given three integers L, D and X.
#
# - determine the minimal integer N such that L≤N≤D and the sum of its digits is X
# - determine the maximal integer M such that L≤M≤D and the sum of its digits is X
#
# Bear will be able to escape from the trap if he correctly determines numbers N 
# and M. The numbers N and M will always exist.
#
# Input
# The first line of input contains the integer L (1≤L≤10000), the number from 
# the task. The second line of input contains the integer D (1≤D≤10000, L≤D), 
# the number from the task. The third line of input contains the integer X (1≤X≤36), 
# the number from the task.
#
# Output
# The first line of output must contain the integer N from the task. The second 
# line of output must contain the integer M from the task.

import sys

inputs = []
for inputstr in sys.stdin:
    inputs.append(int(inputstr))
lower_bound = int(inputs[0])
upper_bound = int(inputs[1])
target_sum_of_digits = int(inputs[2])

min_number_fit = 100000
max_number_fit = 0
for i in range(lower_bound, upper_bound+1):
    digits = str(i)
    digits_sum = sum(int(d) for d in digits)
    if digits_sum == target_sum_of_digits:
        if i < min_number_fit:
            min_number_fit = i
        if i > max_number_fit:
            max_number_fit = i
print(min_number_fit)
print(max_number_fit)



