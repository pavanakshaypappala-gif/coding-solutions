# cook your dish here
n = int(input())
for _ in range(n):
    x,y,z = map(int,input().split())
    if (x>y and x>z):
        print("Alice")
    elif(y>x and y>z):
        print("Bob")
    else:
        print("Charlie")