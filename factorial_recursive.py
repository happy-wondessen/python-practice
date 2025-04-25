def factorial(n):
    if n ==0 or n==1:
        return 1         #Base case which returns 1 if n = 1 or n = 0
    else:
        return n * factorial(n-1)
