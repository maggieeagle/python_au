
# Intervals

+ [Max Consecutive Ones](#problems/max-consecutive-ones)

+ [Squares of a Sorted Array](#problems/squares-of-a-sorted-array)

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
 def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
     count = 0
     max = 0
     for i in nums:
         if i == 1:
             count += 1
         else:
             if count > max:
                 max = count
             count = 0
     if count > max:
                 max = count
     return max

```


## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
 def sortedSquares(self, A: List[int]) -> List[int]:
     for i in range(len(A)):
         A[i] = A[i]*A[i]
     A.sort()
     return A
```

##