# cook your dish here
n = int(input())
for _ in range(n):
    x,y,z = map(int,input().split())
    m = y*z
    if(m>=x):
        print("YES")
    else:
        print("NO")