string = input("Enter the string: ")
lower_string = string.lower()
vowels = "aeiou"
consonents = sum(1 for char in string if char not in vowels)
print(f"""a: {string.count("a")}
e: {string.count("e")}
i: {string.count("i")}
o: {string.count("o")}
u: {string.count("u")}
consonents: {consonents}""")