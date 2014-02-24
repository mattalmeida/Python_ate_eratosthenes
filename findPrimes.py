import sys
import math
import pprint

def pfinder(n):
   
    primes = []
    if n > 2:
        primeDict = dict((k, 'false') for k in range(2,n+1))
        m = 2
        for m in range(2,int(math.sqrt(n))+1):
            for k in primeDict:
                if k != m and k % m == 0:
                     primeDict[k] = 'true'
        for k in primeDict:
            if primeDict[k] == 'false':
                primes.append(k)
        #print primeDict
        print "There are " + str(len(primes)) + " primes under " + str(n) + \
        " and they are: "
        print primes
    else:
        print "Your number is outside of the bounds."

if __name__ == '__main__':
    pfinder(int(sys.argv[1]))
