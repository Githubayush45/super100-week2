def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False

    # Check from 2 to n-1
    for i in range(2, n):
        # If n is divisible by any number in this range, it is not prime
        if n % i == 0:
            return False

    # If no divisors were found, the number is prime
    return True

# Test the function
print(is_prime(7))  # True, because 7 is only divisible by 1 and 7
