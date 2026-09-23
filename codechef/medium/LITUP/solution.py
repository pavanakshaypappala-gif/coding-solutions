# cook your dish here
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    z = list(map(int,input().split()))
    a = 10**9
    for i in range(x):
        for j in range(i+1,x):
            l = min(i-y,j-y)
            r = max(i+y,j+y)
            if l<=0 and r>=x-1:
                a = min(a,z[i]+z[j])
    if a==10**9:
        print("-1")
    else:
        print(a)
    