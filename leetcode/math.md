
# Math


+ [Reverse Integer](#problems/reverse-integer)

+ [Palindrome Number](#problems/palindrome-number)

+ [Fizz Buzz](#problems/fizz-buzz)

+ [Base 7](#problems/base-7)

+ [Fibonacci Number](#problems/fibonacci-number)

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


## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
 def fizzBuzz(self, n: int) -> List[str]:
     out = []
     for i in range(n + 1):
         if i == 0:
             continue
         if i % 3 == 0 and i % 5 == 0:
             out.append("FizzBuzz")
         else:
             if i % 3 == 0:
                 out.append("Fizz")
             else:
                 if i % 5 == 0:
                     out.append("Buzz")
                 else:
                     out.append(str(i))
     return out


```


## Base 7

https://leetcode.com/problems/base-7/

```python
 def convertToBase7(self, num: int) -> str:
     answer = []
     out = ""
     if num < 0:
         out += "-"
         num = abs(num)
     if num == 0:
         return "0"
     remaind = 0
     while num != 0:
         remaind = num % 7
         answer.append(remaind)
         num = num // 7
     answer.reverse()
     for i in answer:
         out = out + str(i)
     return out
```


## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
 def fib(self, N: int) -> int:
     prevprev = 0
     prev = 1
     fi = 0
     if N == 0:
         return 0
     if N == 1:
         return 1
     for i in range(N - 1):
         fi = prevprev + prev
         prevprev = prev
         prev = fi
     return fi
```

##