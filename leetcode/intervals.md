# Intervals


+ [Non-overlapping Intervals](#problems/non-overlapping-intervals)

+ [Merge Intervals](#problems/merge-intervals)

+ [Insert Interval](#problems/insert-interval)

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
 def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
     intervals.sort()
     prev = float("-inf")
     count = 0
     for i in intervals:
         if i[0] >= prev:
             prev = i[1]
         else:
             count+=1
             prev = min(prev, i[1])
     return count
```

## Merge Intervals

https://leetcode.com/problems/merge-intervals/

```python
 def merge(self, intervals: List[List[int]]) -> List[List[int]]:
     intervals.sort()

     if (intervals == []):
         return intervals

     begin_prev = intervals[0][0]
     end_prev = intervals[0][1]

     ans: List[List[int]] = []
     for i in intervals:
         if i[0] > end_prev:
             ans.append([begin_prev, end_prev])
             begin_prev = i[0]
             end_prev = i[1]
         else:
             end_prev = max(end_prev, i[1])
     ans.append([begin_prev, end_prev])
     return ans

```

## Insert Interval

https://leetcode.com/problems/insert-interval/

```python
 def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
     intervals.append(newInterval)
     intervals.sort()
     print(intervals)
     if (intervals == []):
         return intervals
     begin_prev = intervals[0][0]
     end_prev = intervals[0][1]
     ans:
         List[List[int]] = []
     for i in intervals:
         if i[0] > end_prev:
             ans.append([begin_prev, end_prev])
             begin_prev = i[0]
             end_prev = i[1]
         else:
             end_prev = max(end_prev, i[1])
     ans.append([begin_prev, end_prev])
     return ans
```

##