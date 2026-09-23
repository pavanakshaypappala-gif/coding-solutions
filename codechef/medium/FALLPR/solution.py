# cook your dish here
n = int(input())
for _ in range(n):
    x = int(input())
    y = list(map(int,input().split()))
    a = 0
    for i in range(0,len(y)):
        a = a+y[i]
        
    if(a>=0):
        print("YES")
    else:
        print("NO")