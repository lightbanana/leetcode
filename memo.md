## 今回解いた問題と次に解く問題
- 今回解いた問題: 141. Linked List Cycle(https://leetcode.com/problems/linked-list-cycle?envType=problem-list-v2&envId=xo2bgr0r)
- 次に解く問題: 20. Valid Parentheses(https://leetcode.com/problems/valid-parentheses?envType=problem-list-v2&envId=xo2bgr0r)
## Step 1
### 考えたこと
- フロイドの循環検出法を見たことがあったが、とりあえず一度訪れたnodeをsetに保持しておいて、毎回確認する方法が確実なので書いてみる。
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_node = set()
        current_node = head
        if head is None:
            return False
        while True:
            if current_node.next is None:
                return False
            elif current_node.next in visited_node:
                return True
            else:
                visited_node.add(current_node)
                current_node = current_node.next
```
## Step 2
```python

```
## Step 3
```python

```