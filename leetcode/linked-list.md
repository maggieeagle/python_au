# Linked-list


+ [Reverse Linked List](#problems/reverse-linked-list)

+ [Middle of the Linked List](#problems/middle-of-the-linked-list)

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
 def reverseList(self, head: ListNode) -> ListNode:
     tail = None
     while head is not None:
         tmp = head.next
         head.next = tail
         tail = head
         head = tmp
     head = tail
     return head
```

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
 def middleNode(self, head: ListNode) -> ListNode:
     head_copy = head
     count = 0
     while head_copy is not None:
         head_copy = head_copy.next
         count += 1
     for i in range(count//2):
         head = head.next
     return head
```

##