## 今回解いた問題と次に解く問題
- 今回解いた問題:283. Move Zeroes(https://leetcode.com/problems/move-zeroes/)
- 次に解く問題:35. Search Insert Position(https://leetcode.com/problems/search-insert-position/)

## Step 1
### 考えたこと
- if p == right(left):のところ、エッジケースで慎重になるべき。

```python
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(True):
            p = (left + right) // 2
            if nums[p] == target:
                return p
            elif nums[p] < target:
                if p == right:
                    return p + 1
                else:
                    left = p + 1
            elif target < nums[p]:
                if p == left:
                    return p
                else:
                    right = p
```
## Step 2
```python

```
## Step 3
```python

```
