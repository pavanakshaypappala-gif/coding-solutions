# cook your dish here
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    a = x+((x-1)//(y-1))
    print(a)