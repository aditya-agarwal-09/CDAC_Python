cart = ["apple", "banana", "apple", "orange", "banana", "banana"]

i = 0
while i < len(cart):
    if cart[i] in cart[:i]:
        cart.pop(i)
    else:
        i+=1

print(cart)