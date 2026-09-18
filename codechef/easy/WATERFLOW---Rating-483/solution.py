# cook your dish here
n = int(input())
for _ in range(n):
    w,x,y,z= map(int,input().split())
    a = w+(y*z)
    if(x<a):
        print("overFlow")
    elif(x==a):
        print("filled")
    else:
        print("Unfilled")