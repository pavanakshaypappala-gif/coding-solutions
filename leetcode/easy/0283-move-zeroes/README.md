# Move Zeroes

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

 **Note**  that you must do this in-place without making a copy of the array.

 

 **Example 1:** 

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```

 **Example 2:** 

```
Input: nums = [0]
Output: [0]

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

 

 **Follow up:**  Could you minimize the total number of operations done?

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 81.85%)  
**Memory:** 20.4 MB (beats 62.99%)  
**Submitted:** 2026-09-18T15:33:10.945Z  

```py
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        s = 0
        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[i],nums[s]=nums[s],nums[i]
                s +=1
        return nums
        
```

---

[View on LeetCode](https://leetcode.com/problems/move-zeroes/)