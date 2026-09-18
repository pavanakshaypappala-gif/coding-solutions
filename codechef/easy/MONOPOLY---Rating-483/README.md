# MONOPOLY - Rating 483

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-18T10:00:38.135Z  

```py
# cook your dish here
n = int(input())
for _ in range(n):
    w,x,y,z= map(int,input().split())
    a = w+(y*z)
    if(x<a):
        print("overFlow")
    elif(x==a):
        print("filled")
    else:
        print("Unfilled")
```

---

[View on CodeChef](https://www.codechef.com/problems/MONOPOLY)