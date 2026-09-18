# cook your dish here
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    if y*100 <= x*107:
        print("YES")
    else:
        print("NO")