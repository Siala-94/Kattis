import math
import sys

n = int(sys.stdin.readline())

# compute the number of factors of 5 that divide n!
num_factors_of_5 = 0
while n >= 5:
    num_factors_of_5 += n // 5
    n //= 5

# compute n! mod 1000
factorial_mod_1000 = 1
for i in range(2, n+1):
    factorial_mod_1000 = (factorial_mod_1000 * i) % 1000

# divide n! by 10^3
factorial_div_1000 = math.floor(factorial_mod_1000 / 1000)

# check the number of factors of 5
if num_factors_of_5 >= 3:
    print(factorial_div_1000)
else:
    print(factorial_mod_1000)
