no1=int(input("enter the number"))

sum=0

while(no1>0):
    rem=no1%10
    
    no1=no1 // 10
    sum=sum+rem
    if sum>9:
        rem=sum%10    
        sum=sum // 10
        sum=sum+rem

print("the rem of given no",rem)
print("the sum of given no",sum)
