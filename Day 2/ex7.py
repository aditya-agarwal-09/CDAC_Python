"""
Write a program that prompts the user to enter a main text string and a substring. Count how many times the substring appears in the main string without using Python's built-in .count() method.

Sample Input: (User inputs main string "banana" and substring "an")
Sample Output: 2

"""

string = input("enter the main string: ")
sstring = input("enter the substring: ")

count = 0
s_len = len(sstring)

for i in range(len(string) - s_len + 1):
    if string[i:i + s_len] == sstring:
        count+=1

print(count)