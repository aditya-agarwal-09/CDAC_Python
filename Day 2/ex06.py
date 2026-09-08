"""
Write a program that prompts the user for a text string and a shift integer, and encrypts the text using a Caesar cipher. It should shift each alphabetical character in the string by the specified shift number down the alphabet. Maintain uppercase and lowercase characters, and leave spaces or punctuation marks completely unchanged.

Sample Input: (User inputs string "Vinod" and shift 3)
Sample Output: "Ylqrg"
"""


string = input("Enter a string: ")
n = int(input("Enter the shift case number: "))

result = ""

for char in string:
    if char.islower():
        result+= chr((ord(char) - ord('a') + n)%26 + ord('a'))
    elif char.isupper():
        result+= chr((ord(char) - ord('A') + n)%26 + ord('A'))
    else:
        result += char

print("Encrypted: ", result)