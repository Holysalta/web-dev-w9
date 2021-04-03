a=int(input())
b=int(input())
for n in range(a,b+1):
    for i in range ((n/2)+1):
        if(i*i)==n:
            print(n)
        
            