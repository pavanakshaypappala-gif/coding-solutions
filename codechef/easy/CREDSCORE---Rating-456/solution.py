# cook your dish here
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    a = 30*y  
    if (x>=a):
        print("YES")
    else:
        print("NO")