import numpy as np

#problem 1 - Sum of Multiples of 3 and 5 up to a given n
def mult35(n):
    s=0
    for i in range(n):
        if i%3==0 or i%5==0:
            s=s+i
    return s

#problem 2 - Sum of Even Fibbonaci numbers up to a given n
def fibsum(n):
    #construct fib sequence up to n
    i=1
    f=[1,2]
    while f[i] < n:
        f.append(f[i]+f[i-1])
        i=i+1
    del f[i]

    #add even entities
    s=0
    for v in range(len(f)):
        if f[v]%2==0:
            s = s + f[v]
    return(f,s)

#problem 3 - prime factorization
def primefac(n):
    fac = list()
    #if number is even output 2 and divide until not even
    while n%2==0:
        fac.append(2)
        n = n/2
    #after even step above, all remaining factors are odd, so skip 2 to avoid even
    #all composite numbers have a factor between 3 and sqrt(n)
    for i in range(3,int(np.sqrt(n)),2):
        #while i divides n, output i and divide
        while n%i==0:
            fac.append(i)
            n = n/i
    #if i does not divide n, and n > 2, n is now a prime factor
    if n > 2:
        fac.append(n)
    return fac

#problem 4 - largest palindrome product of an s digit number
def palindrome(s):
    #make number out of s many 9 so we can work our way down to find the big one
    a=0
    b=0
    orig = 0
    for i in range(s):
        a = int(str(a)+str(9))
    b = a
    orig = a

    #define function to reverse any number we give it 1234 > 4321, etc.
    def rev(n):
        reverse = 0
        while n>0:
            remainder = n%10
            reverse = reverse*10 + remainder
            n = n//10
        return reverse

    #check if a*b == rev(a*b), if so add it to list to sort
    output = list()
    while 1:
        #decrement a to process all values for a
        while a*b != rev(a*b):
            a = a-1
            if a == 0:
                break
        #create our list when equal
        if a*b == rev(a*b):
            output.append(a*b)
            #a takes the orinal value, b gets decremented to itterate over b
            a = orig
            b = b-1
            if b == 0:
                break
    return max(output)

#probelm 5 - smallest multiple: smallest number to be ebenly divided by 1 to n
def smallestMultiple(n):
    #build out array up to n
    nums = np.empty([1,0])
    for v in range(n+1):
        nums = np.append(nums,v)
    nums = np.delete(nums,[0])
    #set start to something bigger to reduce time, we know it isn't < this
    output = n
    #check if output devides all nums, add the list should be 0 if value found
    while np.sum(np.remainder(output,nums))!=0:
        output = output+n
    return output

#problem 6 - sum square difference for the first n natural numbers
def sumSquare(n):
    #make numpy array of n values
    nums = np.empty([1,0])
    for v in range(n+1):
        nums = np.append(nums,v)

    #find sum of squares
    numsq = np.square(nums)
    sumsq = np.sum(numsq)

    #find square of sum
    numsum = np.sum(nums)
    numsumsq = numsum**2

    #find difference between square of sum and sum of squares
    output = numsumsq - sumsq
    return(int(output))

#problem 7 - 10001st prime - nth prime number calculator
def primeFind(n):
    primes = [2,3,5,7,11,13]
    num = 14
    count = 6
    while count <= n-1:
        for v in primes:
            if num%v == 0:
                num = num+1
                break
            else:
                primes.append(num)
                count = count +1
                num = num+1
                break
    return primes



print(mult35(1000))
print(fibsum(4000000)[1])
print(primefac(600851475143))
# print(palindrome(3))
# print(smallestMultiple(20))
print(sumSquare(100))
print(primeFind(10))
