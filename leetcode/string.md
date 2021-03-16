
# String


+ [Valid Anagram](#problems/valid-anagram)

+ [Reverse String](#problems/reverse-string)

+ [Reverse Vowels of a String](#problems/reverse-vowels-of-a-string)

+ [Reverse Words in a String III](#problems/reverse-words-in-a-string-iii)

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

```python
 def isAnagram(self, s: str, t: str) -> bool:
     s_list = list(s)
     t_list = list(t)
     s_list.sort()
     t_list.sort()
     if s_list == t_list:
         return True
     return False

```


## Reverse String

https://leetcode.com/problems/reverse-string/

```python
 def reverseString(self, s: List[str]) -> None:
     for i in range(len(s)//2):
         tmp = s[i]
         s[i] = s[len(s) - 1 - i]
         s[len(s) - 1 - i] = tmp

```



## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
 def reverseVowels(self, s: str) -> str:
     vowels_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
     vowels = []
     vowels_index = []
     s = list(s)
     for i in range(len(s)):
         if s[i] in vowels_set:
             vowels.append(s[i])
             vowels_index.append(i)
     for i in vowels_index:
         s[i] = vowels.pop()
     return ''.join(s)

```


## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
 def reverseWords(self, s: str) -> str:
     s = list(s)
     word = ''
     answer = ''
     for i in s:
         if i != ' ':
             word += i
         else:
             word = word[::-1]
             for i in word:
                 answer += i
             answer += ' '
             word = ''
     word = word[::-1]
     for i in word:
                 answer += i
     return answer
```

##