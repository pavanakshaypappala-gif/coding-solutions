# cook your dish here
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    a = x%y   
    if(x>=y):
        print(a)
    else:
        print(x)