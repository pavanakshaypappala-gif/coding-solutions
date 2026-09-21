# cook your dish here
n = int(input())
for _ in range(n):
    x = int(input())
    if(x<3):
        print("LIGHT")
    elif(3<=x<7):
        print("MODERATE")
    else:
        print("HEAVY")