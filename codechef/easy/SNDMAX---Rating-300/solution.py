# cook your dish here
n = int(input())
for _ in range(n):
    x,y,z = map(int,input().split())
    sort = [x,y,z]
    sort.sort()
    print(sort[1])