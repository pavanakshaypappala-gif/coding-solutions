# DNATION - Rating 305

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T09:35:14.317Z  

```py
# cook your dish here
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    z = x-y
    if z>=0:
        print(z)
    else:
        print("0")
```

---

[View on CodeChef](https://www.codechef.com/problems/DNATION)