# cook your dish here
n = int(input())
for  _  in range(n):
    x,y = map(int,input().split())
    if(y<x):
        print("0")
    else:
        z = y-x
        print(z)