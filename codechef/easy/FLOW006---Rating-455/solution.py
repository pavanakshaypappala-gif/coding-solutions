# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    digit_sum = 0
    
    while n > 0:
        digit_sum += n % 10
        n //= 10             
        
    print(digit_sum)