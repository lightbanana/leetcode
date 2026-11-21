## Step 1
### 考えたこと
- 深さ優先探索をしたい。実装したことがないので、とりあえずやってみる。stackに積むことだけ聞いたことがあった。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        stack = []
        node_to_depth = dict()
        current_node = root
        stack.append(current_node)
        node_to_depth[current_node] = 1
        while stack:
            current_node = stack.pop()
            left = current_node.left
            right = current_node.right
            if left:
               node_to_depth[left] = node_to_depth[current_node] + 1
               stack.append(left)
            if right:
               node_to_depth[right] = node_to_depth[current_node] + 1
               stack.append(right)
        return max(node_to_depth.values())
```
## Step 2
```python

```
## Step 3
```python

```
