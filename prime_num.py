import math

def is_prime(num):
    isPrime = False
    if(num <= 0 or num == 1):
        return isPrime
    else:
        sqr_num = int(math.sqrt(num))
        for i in range(2, sqr_num+1):
            div = num%i
            if(div == 0):
                isPrime = False
                break
            else:
                isPrime = True
        # isPrime = False
    return isPrime

print(is_prime(73))