# print("Hello World")
#
# x = int(input("Please enter an integer"))
# if x < 0:
#     x = 0
#     print("Negative changed to zero")
# elif x == 0:
#     print("Zero")
# elif x ==1:
#     print("Single")
# else:
#     print("More")
#
output = 0
for i in range(1,101):
    output += i
print(output)

def fib(n):
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b=b,a+b
    return result


print(fib(1000))
