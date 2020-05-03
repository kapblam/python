import numpy as np
import time


# problem 1 - Sum of Multiples of 3 and 5 up to a given n
def mult35(n):
    s = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            s = s + i
    return s


# problem 2 - Sum of Even Fibbonaci numbers up to a given n
def fibsum(n):
    # construct fib sequence up to n
    i = 1
    f = [1, 2]
    while f[i] < n:
        f.append(f[i] + f[i - 1])
        i = i + 1
    del f[i]

    # add even entities
    s = 0
    for v in range(len(f)):
        if f[v] % 2 == 0:
            s = s + f[v]
    return (f, s)


# problem 3 - prime factorization
def primefac(n):
    fac = list()
    # if number is even output 2 and divide until not even
    while n % 2 == 0:
        fac.append(2)
        n = n / 2
    # check for 9
    if n == 9:
        fac.append([3, 3])
        n = 1
    # after even step above, all remaining factors are odd, so skip 2 to avoid even
    # all composite numbers have a factor between 3 and sqrt(n)
    for i in range(3, int(np.rint(np.sqrt(n))), 2):
        # while i divides n, output i and divide
        while n % i == 0:
            fac.append(i)
            n = n / i
    # if i does not divide n, and n > 2, n is now a prime factor
    if n > 2:
        fac.append(n)
    return fac


# problem 4 - largest palindrome product of an s digit number
def palindrome(s):
    # make number out of s many 9 so we can work our way down to find the big one
    a = 0
    b = 0
    orig = 0
    for i in range(s):
        a = int(str(a) + str(9))
    b = a
    orig = a

    # define function to reverse any number we give it 1234 > 4321, etc.
    def rev(n):
        reverse = 0
        while n > 0:
            remainder = n % 10
            reverse = reverse * 10 + remainder
            n = n // 10
        return reverse

    # check if a*b == rev(a*b), if so add it to list to sort
    output = list()
    while 1:
        # decrement a to process all values for a
        while a * b != rev(a * b):
            a = a - 1
            if a == 0:
                break
        # create our list when equal
        if a * b == rev(a * b):
            output.append(a * b)
            # a takes the orinal value, b gets decremented to itterate over b
            a = orig
            b = b - 1
            if b == 0:
                break
    return max(output)


# probelm 5 - smallest multiple: smallest number to be evenly divided by 1 to n
def smallestMultiple(n):
    # build out array up to n
    nums = np.empty([1, 0])
    for v in range(n + 1):
        nums = np.append(nums, v)
    nums = np.delete(nums, [0])
    # set start to something bigger to reduce time, we know it isn't < this
    output = n
    # check if output divides all nums, add the list should be 0 if value found
    while np.sum(np.remainder(output, nums)) != 0:
        output = output + n
    return output


# problem 6 - sum square difference for the first n natural numbers
def sumSquare(n):
    # make numpy array of n values
    nums = np.empty([1, 0])
    for v in range(n + 1):
        nums = np.append(nums, v)

    # find sum of squares
    numsq = np.square(nums)
    sumsq = np.sum(numsq)

    # find square of sum
    numsum = np.sum(nums)
    numsumsq = numsum ** 2

    # find difference between square of sum and sum of squares
    output = numsumsq - sumsq
    return (int(output))


# problem 7 - 10001st prime - nth prime number calculator
# Don't use
def primeFind(n):
    primes = [2, 3, 5, 7]
    num = 9
    count = 3
    while count < n - 1:
        flag = 0
        for v in range(len(primes)):
            mod = [num % x for x in primes]
            if mod[v] == 0:
                flag = 1
        if flag:
            num = num + 2
        elif not flag:
            primes.append(num)
            num = num + 2
            count = count + 1
    return primes[n - 1]


# same thing as problem 7 above just using prime factorization instead
# note this method is orders of magnitude quicker than the direct approach above.
# USE THIS INSTEAD of primeFind()!
# Don't use
def primeFindFact(n):
    primes = [2]
    num = 3
    count = 0
    while count < n - 1:
        if primefac(num) == [num]:
            primes.append(num)
            num = num + 2
            count = count + 1
        else:
            num = num + 2
    return primes[n - 1]


# interesting method for #7 on the internet -- this soulution is correct - investigate other methods.
def primefind2(n):
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if all(attempt % x != 0 for x in primes):
            primes.append(attempt)
        attempt += 2

    return primes[n - 1]


# Problem 8 - Largest product in given series using n adjacent digits
def largeProductInSeries(n):
    start = time.time()
    series = str(
        "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450")
    output = 1
    prod = 1
    for i in range(len(series) - n):
        for j in range(n):
            prod = prod * int(series[j + i])
        if prod > output:
            output = prod
        prod = 1
    print("Runtime: %.7f" % (time.time() - start))
    return output


# Problem 9: Special Pythagorean Triplet: there exists exactly one Pythagorean triplet for which
# a+b+c=1000. Find the product abc.
def problem9():
    start = time.time()
    cap = 500
    for i in range(cap):
        for j in range(i, cap, 1):
            for k in range(j, cap, 1):
                if i ** 2 + j ** 2 == k ** 2 and i + j + k == 1000:
                    output = [i * j * k, i, j, k]

    print("Runtime: %.7f" % (time.time() - start))
    return output


# Problem 10: Summation of Primes.  Find sum of all primes below 2 million:
# note: takes a VERY long time to run, but the answer 142913828922 is correct!
def problem10(n):
    start = time.time()
    # took from primefind2() above:
    primes = [2]
    attempt = 3
    output = 0
    while primes[-1] < n:
        if all(attempt % x != 0 for x in primes):
            primes.append(attempt)
        attempt += 2
    for i in range(len(primes) - 1):
        output += primes[i]
    print("Runtime: %.7f" % (time.time() - start))
    return output


# Problem 10 again, but let's try using the Sieve of Eratosthenes:  Does not finish in reasonable 
# time (waiting 1hr plus...)
def sieveOfEratosthenes(n):
    # Generate list of numbers from 2 to n.  Remember 1 is NOT a prime number
    start = time.time()
    nums = list()
    rmv = list()
    for i in range(2, n + 1):
        nums.append(i)
    # starting from 2 find all multiples then iterate the multiple until no multiples are left:
    p = 2

    while len(nums)-nums.index(p) > p in nums:
        for i in nums:
            if i != p and i % p == 0:
                rmv.append(i)
        for i in rmv:
            nums.remove(i)
        p = nums[nums.index(p)+1]
        rmv = list()
        sum = 0
    for i in nums:
        sum += i
    print("Runtime: %.7f" % (time.time() - start))
    return sum



# print(mult35(1000))
# print(fibsum(4000000)[1])
# print(primefac(600851475143))
# print(palindrome(3))
# print(smallestMultiple(20))
# print(sumSquare(100))
# print(primeFindFact(10001))
# print(primeFind(10001))
# print(primefind2(20001))
print(largeProductInSeries(13))
# print(problem9())
# print(problem10(2000000))
# print(sieveOfEratosthenes(2000000))
