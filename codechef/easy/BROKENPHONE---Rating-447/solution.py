# cook your dish here
n = int(input())
for _ in range(n):
    w,x,y,z = map(int,input().split())
    a = w-y
    b = x-z
    if(a<b):
        print("First")
    elif(a==b):
        print("Any")
    else:
        print("Second")