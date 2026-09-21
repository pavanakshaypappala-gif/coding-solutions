# cook your dish here
n = int(input())
for _ in range(n):
    x,y,z=map(int,input().split())
    w = x+y
    if w==z:
        print("YES")
    else:
        print("NO")