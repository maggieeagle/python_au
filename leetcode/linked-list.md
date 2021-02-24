# Linked-list


+ [Reverse Linked List](#problems/reverse-linked-list)

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

##