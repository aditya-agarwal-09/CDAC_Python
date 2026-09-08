score = float(input("enter the score: "))

if(score < 60):
    print("F")
elif score >= 60 and score <= 69:
    print("D")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 80 and score <= 89:
    print("B")
else:
    print("A")