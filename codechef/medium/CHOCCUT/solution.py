# cook your dish here
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    a = x*y
    if(a%2==0):
        print("Yes")
    else:
        print("No")