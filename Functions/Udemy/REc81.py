def factorial(x):
    if(x==1):
        return 1
    else:
        return x*(factorial(x-1))

res=factorial(5)
print(res)