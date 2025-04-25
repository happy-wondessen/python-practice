def factorial(n):
    fact = 1  # Initialize fact to 1.
    while n > 0:  # Checks if n is greater than 0, if true continues multiplying
        fact = fact * n  # Multiplies fact by n
        n = n - 1  # Decreases n by 1 after the iteration
    return fact



