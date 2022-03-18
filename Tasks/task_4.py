def fibo(x):
    if x == 1 or x==2:
        return 1
    else:
        return(fibo(x-1) + fibo(x-2))

num = 6
print("The fibonacci value of", num, "is", fibo(num))

