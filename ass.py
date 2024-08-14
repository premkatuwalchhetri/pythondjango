# prime or composite
def is_prime(n):
 if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_prime_or_composite(number):
    if number <= 1:
        print(f"{number} is neither prime nor composite.")
    elif is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is a composite number.")