# cook your dish here
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    top = 10*x+90*y
    print(top)