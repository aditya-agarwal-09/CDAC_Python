message = input("Enter the message to be encrypted: ")
words = message.split()

rev_words = [word[::-1] for word in words]
result = " ".join(rev_words)

print(result)
