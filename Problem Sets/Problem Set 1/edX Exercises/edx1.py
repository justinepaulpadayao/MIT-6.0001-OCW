# # Problem 1
# # (10/10 points)
# # Assume s is a string of lower case characters.
# # Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# # For example, if s = 'azcbobobegghakl', your program should print:
# # Number of vowels: 5

# vowels = ['a','e','i','o','u']
# count = 0

# s = 'How to succeed'

# for char in s:
#     if char in vowels:
#         count += 1
        
# print(count)


# # Problem 2
# # (10/10 points)
# # Assume s is a string of lower case characters.
# # Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your
# # program should print
# # Number of times bob occurs is: 2

# s = 'azcbobobegghakl'
# bob = 'bob'
# count = 0

# # for i in range(len(s)):                                     # for loop variable
# #     if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':     # Indexing into strings
# #         count += 1                                          # Counter
# # print(count)

# for i in range(len(s)):
#     print (s[i:i+3])
#     if s[i:i+3] == 'bob':
#         count += 1
# print(count)

  
# # Problem 3

# # (15/15 points)
# # Assume s is a string of lower case characters.

# # Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if
# # s = 'azcbobobegghakl', then your program should print:
# # Longest substring in alphabetical order is: beggh

# # In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
# # Longest substring in alphabetical order is: abc

# # Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we
# # suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and
# # cleared your head.


# # Pseudocode
# # Print the characters
# # For each character, check if the succeeding character is alphabetical
# # Add character to the substring variable


s = 'azcbobobegghakl'
current = ''
longest = ''

for i in range(len(s)):
    if s[i] >= s[i-1]:
        current += s[i]
        if len(current) > len(longest):
            longest = current
    else:
        current = s[i]
print(longest)
    
