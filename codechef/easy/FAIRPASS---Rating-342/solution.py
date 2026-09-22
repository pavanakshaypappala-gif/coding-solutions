# cook your dish here
n = int(input())
for _ in range(n):
    N,K = map(int,input().split())
    if(N<K):
        print("YES")
    else:
        print("NO")