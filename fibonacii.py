n=int(input('Number of elements in fibonacii series: '))
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(3,n):
        sum=a+b
        print(sum)
        a=b
        b=sum
        
