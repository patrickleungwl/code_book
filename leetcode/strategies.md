## Resources

[Curated Python Algos and Libraries](https://github.com/vinta/awesome-python/blob/master/README.md#algorithms-and-design-patterns)


## Strategies

--

[Two Sum](https://leetcode.com/problems/two-sum/) (simple)

Given a list of integers- and a target, return the indicies of the two numbers
that add up to target.

*Instead of 1) brute force making two passes or 2) building a hash map, 
just build a hash map of each integer location- and while doing that, 
check back to see if the integer's complement already exists in the cache. 
If so, return the two integers' location immediately- resulting in a 
one-pass solution- O(n)- we only look up each list element exactly once.*

--

[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

Given two numbers- where each number is a linked list of digit nodes.  
Write a function to add the two list of digits.

*Iterate through the digits from each list.  Remember to increment 
a carry digit.  For each result digit, add a new digit node.*

--

[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Given a string, find the length of the longest substring without repeating
characters.

*Iterate through the input string.  Keep a cache of the cached characters so far. 
If we see a repeat, start over from the first index (place) of the repeated character.
And record the longest string so far.*

--

[Longest Palindrome Substring](https://leetcode.com/problems/longest-palindromic-substring/)

Given a string, find the longest palindromic substring.

*Definitely need to avoid double loops.  Make one scan only.  Given a scan index
position, probe to the left and right to see if the string at that string index
is a palindrome.  Need to probe for two palindrome conditions- one with even number of
characters (abba) and one with an odd number of characters (racecar).  The probe 
check functions need to check for string boundaries.*

--

[Reverse Integer](https://leetcode.com/problems/reverse-integer/) (simple)

Given a 32-bit signed integer, reverse digits of an integer. 

*Strip off each digit of the input integer one at a time using the mod % operator by 10
to get the rightmost digit.  Multiple that digit by 10 and add to resulting number.
Also remember to check for negative conditions.  And also for boundary max and min integers.*

--

[Palindrome Number](https://leetcode.com/problems/palindrome-number/) (simple)

Determine whether an integer is a palindrome. An integer is a palindrome when it 
reads the same backward as forward.

*The key insight is to strip the rightmost digit one by one- using the mod % operator by 10
and putting the digits into a vector.  Then we scan the vector from both left and right
and compare the digits.  If the digits do not match, then immediately we know the integer 
is not a palindrome.*

--

[Roman To Integer](https://leetcode.com/problems/roman-to-integer) (simple)

Given a roman numeral, convert it to an integer.

*Read the roman numeral from left to right.  Straight forward letter for letter conversion
to number values- with exceptions needed for I before V and X, X before D and C and so on.
For the exception cases, must peek ahead forward by 1 char- and if indeed is IV case,
then I is a -1 instead of a +1 and so on.*

