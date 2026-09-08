"""

Write a program that accepts a string input from the user and outputs it in Title Case (capitalizing the first letter of each word and lowercasing the remaining letters).
 Do not use Python's built-in .title() method.

Sample Input: "WELCOME TO BANGALORE CITY"
Sample Output: "Welcome To Bangalore City

"""


word = input("Enter a string: ")

sentence = word.split()
title_word = ""

for string in sentence:
    up = string.upper()[0] + string.lower()[1:]
    title_word = title_word + up + " "

title_word = title_word.strip(' ')
print(title_word)
    
