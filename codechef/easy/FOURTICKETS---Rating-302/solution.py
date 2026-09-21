# cook your dish here
n = int(input())
for _ in range(n):
    x = int(input())
    y = x*4
    if y>1000:
        print("NO")
    else:
        print("YES")