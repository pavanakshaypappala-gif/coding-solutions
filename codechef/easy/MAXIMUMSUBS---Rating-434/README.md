# MAXIMUMSUBS - Rating 434

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T08:32:52.824Z  

```py
# cook your dish here
n = int(input())
for  _ in range(n):
    x,y,z = map(int,input().split())
    if(x>y and x>z):
        print("Setter")
    elif(y>x and y>z):
        print("Tester")
    else:
        print("Editorialist")
```

---

[View on CodeChef](https://www.codechef.com/problems/MAXIMUMSUBS)