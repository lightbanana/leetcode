## 今回解いた問題と次に解く問題
- 今回解いた問題:283. Move Zeroes(https://leetcode.com/problems/move-zeroes/)
- 次に解く問題:35. Search Insert Position(https://leetcode.com/problems/search-insert-position/)

## Step 1
### 考えたこと
- ナイーブにやるなら、numsを前から走査して、もう一つ配列を用意して0以外の数字を見たら前から入れていく。0の出てきた回数も数えておいて、最後に0をその個数分だけ入れる。
- nums = nums_cpにすると、参照渡しになってしまう。

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_cp = []
        zero_count = 0
        for _, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            else:
                nums_cp.append(num)
        for _ in range(zero_count):
            nums_cp.append(0)
        for i in range(len(nums)):
            nums[i] = nums_cp[i]
```
## Step 2
```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        for num in nums:
            if num != 0:
                nums[write] = num
                write += 1
        for i in range(write, len(nums), 1):
            nums[i] = 0
```
## Step 3
```python

```
