## 今回解いた問題と次に解く問題

## Step 1
### 考えたこと

```python
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set()
        intersection = list()
        for i, num in enumerate(nums1):
            if num not in seen:
                seen.add(num)
        for i, num in enumerate(nums2):
            if num in seen and num not in intersection:
                intersection.append(num)
        return intersection
```
## Step 2
```python

```
## Step 3
```python

```
