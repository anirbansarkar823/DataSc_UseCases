# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 00:05:24 2020

@author: Anirban
"""

# Reference
# https://www.programiz.com/python-programming/regex
import re

pattern = '^a...s$' 
# pattern depicts any 5 letter word starting with 'a' and ending with 's'

test_str = 'abyss'
result = re.match(pattern, test_str)
print('match' if result else 'not match')


# MetaCharacters
'''
[] . ^ $ * + ? {} () \ |

[] - Square brackets - a set of character we wish to match
^ - caret - checks if a string 'starts with' a certain character
. - Period - matches any single character (except '\n')
$ - Dollars - checks if a string 'ends with' a certain character
* - Star - matches 'zero or more occurrences' of the pattern left to it.
+ - Plus - matches 'one or more occurrences' of the pattern left to it
? - Question Mark - matches 'zero or one occurrence' of the pattern left to it.
{} - Braces - eg:{n,m} means at least 'n', and at most 'm' repetitions(continuous) of the pattern left to it a{2,3}
| - Alternation - used for alternation ('or' operator)
() - Group - is used to group sub-patterns  
\ - Backslash - escape various characters including all metacharacters



# [] - specifies a set of characters we wish to match
# [abc] - match is any among 'a', 'b' or 'c' occurs
# [a-e] - matches any characters out of a to e
# [^abc] - means any character except a, b or c



# () - Group
# (a|b|c)xz -- matches any string that starts with either a or b or c but followed by xz
'''


# Special Sequences
'''
\A - matches if specified characters are at the start of a string. eg: \Athe; the sun - 1 Match

\b - Matches if the specified characters are at the beginning or end of a word. 

\B - Opposite of \b. Matches if the specified characters are not at the beginning or end of a word.

\d - Matches any decimal digit. Equivalent to [0-9]

\D - Matches any non-decimal digit. Equivalent to [^0-9]

\s - Matches where a string contains any whitespace character. Equivalent to [ \t\n\r\f\v] eg: 'Python RegEx' - 1 match

\S - Matches where a string contains any non-whitespace character. Equivalent to [^ \t\n\r\f\v]

\w - Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_].

\W - Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]

'''

# 1. re.findall() - returns a list of strings containing all matches
string = 'hello 12 hi 89.'
pattern = '\d+' 
print(re.findall(pattern, string))
# ['12', '89']


# 2. re.split() - splits the string where there is a match and returns all the splitted strings
string = 'hello 12 hi 89.'
pattern = '\d+' 
print(re.split(pattern, string))
# ['hello ', ' hi ', '.']

# in re.split(), maxsplit specifies the max number of splits
# putting maxsplit = 1
print(re.split(pattern, string, 1))
# ['hello ', ' hi 89.']



# 3. re.sub() - [substitute] matched occurrences are replaced with the content of replace_str
# re.sub(pattern, replace_str, string)
string = 'abc 12\
    de 23 \n f45 6'
    
# pattern to match all whitespace characters
pattern = '\s+'

#empty string
replace = ''

new_string = re.sub(pattern, replace, string)
print(new_string)
# if pattern is not found, re.sub() returns the original string



# 4. re.subn()
# similar to re.sub() except it returns a tuple of 2 items containing the new string and the number of substitution made
string = 'abc 12\
    de 23 \n f45 6'
    
# pattern to match all whitespace characters
pattern = '\s+'

#empty string
replace = ''

new_string = re.subn(pattern, replace, string)
print(new_string)




# 5. re.search(pattern, str) -- looks for the first location where the RegEx pattern produces a match with the string
string = 'Python is fun'

# we will check if 'Python' is at the beginning
# \A - to specify the string must start with 'Python'
match = re.search('\APython',string)

if match:
    print('pattern found')
else:
    print('pattern not found')
    
    
    
# 6. match.group() returns the part of the string where there is a match
string = '39801 35 6 , 2102 1111'

# pattern to detect a 3 digit number followed by a space followed by  2 digit number and followed by space
pattern = '(\d{3}) (\d{2}) '
match = re.search(pattern, string)
if match:
    print(match.group())
else:
    print('no match found')
    
