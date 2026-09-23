# BROKENPHONE - Rating 447

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T09:01:36.107Z  

```py
# cook your dish here
n = int(input())
for _ in range(n):
    w,x,y,z = map(int,input().split())
    a = w-y
    b = x-z
    if(a<b):
        print("First")
    elif(a==b):
        print("Any")
    else:
        print("Second")
```

---

[View on CodeChef](https://www.codechef.com/problems/BROKENPHONE)