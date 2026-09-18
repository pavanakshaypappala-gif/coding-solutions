# cook your dish here
n = int(input())
for _ in range(n):
    x,y,z = map(int,input().split())
    m = x+y  
    if (m <= z):
        print("2")
    elif(x<=z):
        print("1")
    else:
        print("0")