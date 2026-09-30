# cook your dish here
n = int(input())
for _ in range(n):
    x,y,z = map(int,input().split())
    o = set(map(int,input().split()))
    a = []
    for _ in range(z):
        for s in range(1,x+1):
            if s not in o:
                a.append(s)
                o.add(s)
                break 
    print(*a)