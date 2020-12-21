## Strategies

---

[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

Given two numbers- where each number is a linked list of digit nodes.  
Write a function to add the two list of digits.

*Iterate through the digits from each list.  Remember to increment 
a carry digit.  For each result digit, add a new digit node.*

---

[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Given a string, find the length of the longest substring without repeating
characters.

*Iterate through the input string.  Keep a cache of the cached characters so far. 
If we see a repeat, start over from the first index (place) of the repeated character.
And record the longest string so far.*

---

[Longest Palindrome Substring](https://leetcode.com/problems/longest-palindromic-substring/)

Given a string, find the longest palindromic substring.

*Definitely need to avoid double loops.  Make one scan only.  Given a scan index
position, probe to the left and right to see if the string at that string index
is a palindrome.  Need to probe for two palindrome conditions- one with even number of
characters (abba) and one with an odd number of characters (racecar).  The probe 
check functions need to check for string boundaries.*

