def fib(n):
    series = [0,1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[:n]
n = int(input("enter a number: "))
print(f"fibanocci: {fib(n)}")

