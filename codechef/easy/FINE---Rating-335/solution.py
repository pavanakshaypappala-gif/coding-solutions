# cook your dish here
n = int(input())
for _ in range(n):
    x = int(input())
    if x<=70:
        print("0")
    elif(70<x<=100):
        print("500")
    else:
        print("2000")