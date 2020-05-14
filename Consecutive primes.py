from math import floor


x = 100



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
    
    maxim = 1
    current = 0
    #print(primes)
    
    for i in range(0, len(primes) - 3):
        summ = primes[i]
        counter = 0
   
        
        for j in range(i, len(primes) - 3):
          

            
            summ += primes[j + 1]
            if(binary_search(primes, summ)):

                current = j + 1 - i + 1
                if current > maxim:
                    maxim = current
                    prm = summ
                    

                
                
    
    return maxim, prm
    

print(consec_primes(primes, consecutive))
