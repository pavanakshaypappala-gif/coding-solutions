# cook your dish here
n = int(input())
for  _ in range(n):
    x,y = map(int,input().split())
    p = x+(x*0.1)
    l = x-y 
    t = p-l
    print(int(t))