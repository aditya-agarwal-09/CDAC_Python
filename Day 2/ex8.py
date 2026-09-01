"""
Write a program that prompts the user to enter a full name (first name, middle name, last name) and anonymizes it. The output should print the initials of the first and middle names followed by the full last name. If the name consists of only a single word, print it as-is.

Sample Input: "Vinod Kumar Kayartaya"
Sample Output: "V. K. Kayartaya"
Sample Input: "Bangalore"
Sample Output: "Bangalore"

"""

name = input("Enter the name: ")

l = name.split()

if(len(l) == 1):
    print(name)
else:
    anon = ""
    for i in l[:-1]: 
        anon += i[0].upper() + "."
    result = anon + l[-1]

print(result)