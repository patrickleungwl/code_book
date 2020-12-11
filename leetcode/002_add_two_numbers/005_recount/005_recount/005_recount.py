# Input
# The input consists of a single test case, which is a list of votes cast. 
# Each line in the input contains the name of a candidate for whom a vote 
# was cast. A name may consist of multiple words, separated by spaces. 
# Words contain letters or hyphens, but no other punctuation characters. 
# There will be at least 2 votes on the list. The list of votes ends with 
# a single line containing the characters ***. This line should not be counted. 
# There can be up to 100000 valid votes.
#
# Output
# If a candidate obtained a simple or absolute majority of all votes cast 
# (that is, more than any other candidate), output the name of this candidate! 
# If no candidate obtained a simple majority, output: “Runoff!” (don’t forget 
# to include the exclamation mark!)
#

import sys

candidates = {}
for inputstr in sys.stdin:
    inputstr = inputstr.strip()
    if inputstr == "***":
        break;
    if inputstr in candidates:
        candidates[inputstr] += 1
        #print("%s %i" % (inputstr, candidates[inputstr]))
    else:
        candidates[inputstr] = 1
        #print("%s %i" % (inputstr, candidates[inputstr]))
    
# count votes for each candidate
#print(candidates)
leader = ""
top_number_of_votes = -1
tied = False
for c in candidates:
    votes_for_c = candidates[c]
    if votes_for_c > top_number_of_votes:
        leader = c
        top_number_of_votes = votes_for_c
        tied = False
        #print("leader %s %i" % (c, top_number_of_votes))
    elif votes_for_c == top_number_of_votes:
        tied = True
        #print("Tied")

if tied==True:
    print("Runoff!")
else:
    print(leader)

