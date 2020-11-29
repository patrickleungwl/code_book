# https://open.kattis.com/problems/tarifa
#
# Pero has negotiated a Very Good data plan with his internet provider. 
# The provider will let Pero use up X megabytes to surf the internet per
# month. Each megabyte that he doesn’t spend in that month gets transferred 
# to the next month and can still be spent. Of course, Pero can only spend 
# the megabytes he actually has.

# If we know how much megabytes Pero has spent in each of the first N months 
# of using the plan, determine how many megabytes Pero will have available in
# the N+1 month of using the plan.

# Input
# The first line of input contains the integer X (1≤X≤100). The second line of 
# input contains the integer N (1≤N≤100). Each of the following N lines contains 
# an integer Pi (0≤Pi≤10000), the number of megabytes spent in each of the first 
# N months of using the plan. Numbers Pi will be such that Pero will never use 
# more megabytes than he actually has.

# Output
# The first and only line of output must contain the required value from 
# the task.

# 10
# 3
# 4
# 6
# 2
#
# First line = number of minutes each month
# Second line = number of months

import sys

inputs = []
for inputstr in sys.stdin:
    inputs.append(int(inputstr))

mins_per_month = inputs[0]
num_months = inputs[1]
min_used = sum(minutes for minutes in inputs[2:])
min_accumulated = sum(mins_per_month for r in range(0,num_months+1))
print(min_accumulated-min_used)


