def main():
    n = int(input("enter a number: "))

    if( n <= 0):
        print("enter a positive number-")


    last = n//2
    d = 2

    while(d <= last):
        if(n % d == 0):
            print("it is not a prime number")
            break
        d+=1    
    else:
        print("it is a prime number")

main()


