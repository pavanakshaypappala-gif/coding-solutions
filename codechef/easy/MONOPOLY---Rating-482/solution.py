# cook your dish here
n = int(input())
for _ in range(n):
    x,y,z = map(int,input().split())
    if(x==y and y==z and z==x):
        print("No")
    elif(x+y<z or x+z<y or z+y<x):
        print("Yes")
    else:
        print("No")