
# Math


+ [Reverse Integer](#problems/reverse-integer)

+ [Palindrome Number](#problems/palindrome-number)

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

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
 def isPalindrome(self, x: int) -> bool:
     symbols = list(str(x))
     length = len(str(x))
     while length > 0:
         if symbols[0] != symbols[length - 1]:
             return False
         if length <= 1:
             return True
         del symbols[0]
         del symbols[length - 2]
         length -= 2
     return True

```

##