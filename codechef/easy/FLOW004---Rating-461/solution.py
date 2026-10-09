# cook your dish here
n = int(input())
for _ in range(n):
    x = input().strip()
    a = int(x[0])+int(x[-1])
    print(a)