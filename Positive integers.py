list=[]
n=int(input('Number of elements: '))
for i in range(0,n):
    a=int(input('Input an integer: '))
    list.append(a)
for i in range(0,len(list)):
    if list[i]>0:
        print(list[i])
