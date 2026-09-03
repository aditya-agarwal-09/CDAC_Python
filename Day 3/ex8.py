"""
Scenario: An online shopping cart has duplicate items due to double-clicks: ["apple", "banana", "apple", "orange", "banana", "banana"]. 
Write a program that processes the list and removes all duplicate items, but keeps the first occurrence of each item in its original order. Print the cleaned cart.

Hardcoded Input: cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
Sample Output: ['apple', 'banana', 'orange']

"""

def main():
    ...
    cart = ["apple", "banana", "apple", "orange", "banana", "banana"]

    i = 0
    while i < len(cart):
     if cart[i] in cart[:i]:
        cart.pop(i)
     else:
        i += 1

    print(cart)
main()
