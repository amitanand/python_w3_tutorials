# Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.

def primeNum(n):
    if n<0:
        print("Negative number provided. Not applicable")
    elif (n>0):
        if n ==2:
            print("Smallest Prime Number")
        else:
            for i in range(3,n):
                if (n%i) == 0:
                    print("Not a prime number")
                    break
    else:
        print("Prime Number")

primeNum(9)