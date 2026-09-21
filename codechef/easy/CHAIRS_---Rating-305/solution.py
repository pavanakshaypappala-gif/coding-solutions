# cook your dish here
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    z = x-y
    if z>=0:
        print(z)
    else:
        print("0")