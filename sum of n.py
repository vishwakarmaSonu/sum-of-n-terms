import time
initial =time.time()
#no time is consumed till infinity
def fun(n):
    return n*(n+1)/2
print(fun(10000000000000000000000000000000000000))
print("time ", time.time()-initial)

# time is consumed
def fun1(n):
    sum = 0
    for i in range (1,n+1):
        sum = sum+i
    return sum
print(fun1(1000000))
print("time ", time.time()-initial)


#more time is comsumed  here
def fun3(n):
    sum =0
    for i in range(1,n+1):
        for j in range(1,n+i):
            sum = sum+1
    return sum
print(fun3(10000))
print("time ", time.time()-initial)
