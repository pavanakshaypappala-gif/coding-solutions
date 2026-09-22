# cook your dish here
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    a = x/2
    if (y>=a):
        print("YES")
    else:
        print("NO")
    