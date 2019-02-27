#From the 2019 competition
#Slow but functional

averages = []
n = int(input())

for x in range(n):
    averages.append(int(input()))

primes = [2]

for i in range(3,max(averages)*2):
    isPrime = True
    for p in primes:
        if i%p==0:
            isPrime = False
            break
    if isPrime == True:
        primes.append(i)

foundPrimes = []
for average in averages:
    found = False
    a = average
    b = average
    count = 0
    while found == False:
        p = primes[count]
        a = 2*average-p
        
        if p == 2*average-a and a in primes:
            b = p
            found = True
        count += 1
    foundPrimes.append([b,a])

for foundPair in foundPrimes:
    for p in foundPair:
        print(p, end = " ")
    print()
