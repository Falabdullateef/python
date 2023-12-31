# So I came across a question which is to find the number of composites generated by the polynomial n^2+41n+41
# Lazy me decided to write a program to do it for me instead of doing it algebraically
# Enjoy :)
# Note: ive made a better version in Java, check it out in my java repo
# Link: https://github.com/Falabdullateef/Java/Math

from functools import reduce
from math import sqrt
def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

prime_counter = 0
startwith = 0
endwith = 10000

for n in range(startwith, endwith+1):
    polynomial = n*n+41*n+41
    res = factors(polynomial)
    if factors(polynomial) == {1, polynomial}:
        prime_counter += 1
    print(f"n={n}, f(n) = {polynomial} {res}")

print(f"there are total {int(endwith-prime_counter)} composites")
print(f"there are total {prime_counter} primes")
