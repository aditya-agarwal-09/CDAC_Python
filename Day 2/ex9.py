"""
Write a program that prompts the user to enter a text string and finds the longest substring within it that reads the same forward and backward. If there are multiple palindromic substrings of the same maximum length, print any one of them.

Sample Input: "babad"
Sample Output: "bab" (or "aba")
Sample Input: "cbbd"
Sample Output: "bb"

"""

string = input("Enter a string: ")

def is_palindrome(s):
    return s == s[::-1]

longest = ""

for i in range(len(string)):
    for j in range(i+1, len(string) + 1):
        substring = string[i:j]
        if(is_palindrome(substring) and len(substring) > len(longest)):
            longest = substring

print(longest)