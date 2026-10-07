# Intersection of Two Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two integer arrays `nums1` and `nums2`, return  *an array of their intersection*. Each element in the result must be  **unique**  and you may return the result in  **any order**.

 

 **Example 1:** 

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

```

 **Example 2:** 

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

```

 

 **Constraints:** 

- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

## Solution

**Language:** Python  
**Runtime:** 11 ms (beats 18.39%)  
**Memory:** 19.4 MB (beats 12.38%)  
**Submitted:** 2026-10-07T06:30:52.110Z  

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for val in nums1:
            if val in nums2:
                result.append(val)
        unique = list(set(result))
        return unique      
```

---

[View on LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/)