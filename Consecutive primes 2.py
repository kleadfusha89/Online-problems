from math import floor


x = 20


primes = []
consecutive = []



def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2, n):
            if n % i == 0:
                status = False
    return status


for n in range(1, x):
    if is_prime(n):

        primes.append(n)

def binary_search(primes, search):
    n = len(primes)
    left = 0
    right = n - 1

    while left <= right:
        mid = floor((left + right)/2)

        if primes[mid] < search:
            left = mid + 1
        elif primes[mid] > search:
            right = mid - 1
        else:
            return True
    return False
        


def consec_primes(primes, consecutive):
    summ = []
    maxim = 1
    current = 0
    add = primes[0]
    print(primes)
    
    for i in range(0, len(primes) - 1):
        add += primes[i + 1]
        summ.append(add)
        counter = 0

    index = 0
    print(summ)
    #for j in range(0, len(summ - 1)):
    print(summ[3]-summ[0])
        
        
    
consec_primes(primes, consecutive)
