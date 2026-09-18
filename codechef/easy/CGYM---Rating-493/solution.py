# cook your dish here
n = int(input())
for _ in range(n):
    a,b,c,d = map(int,input().split())
    if (a+b>=d or b+c>=d or a+c >=d):
        print("YES")
    else:
        print("NO")