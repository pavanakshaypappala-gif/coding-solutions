# cook your dish here
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    a = x*100
    b = y*10 
    if(a>=b):
        print("Cloth")
    else:
        print("Disposable")