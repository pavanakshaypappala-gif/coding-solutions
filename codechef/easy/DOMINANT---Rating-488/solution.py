# cook your dish here
n = int(input())
for _ in range(n):
    x,y,z = map(int,input().split())
    if(x > y+z or y>x+z or z>x+y):
        print("YES")
    else:
        print("NO")