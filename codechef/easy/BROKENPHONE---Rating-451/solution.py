# cook your dish here
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    if (x<y):
        print("REPAIR")
    elif(x==y):
        print("ANY")
    else:
        print("NEW PHONE")