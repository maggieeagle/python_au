
# Math


+ [Reverse Integer](#problems/reverse-integer)

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
 def reverse(self, x: int) -> int:
     out = ""
     sign = ""
     if x < 0:
         sign = "-"
     ans = list(str(abs(x)))
     ans.reverse()
     for i in ans:
         out += str(i)
     out = out.lstrip('0')
     if out == "":
         out = "0"
     if int(out) > pow(2, 31) or int(out) < -pow(2, 31):
         return 0
     return sign + out

```

##