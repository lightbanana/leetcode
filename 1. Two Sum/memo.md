問題は1. Two Sum(https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=xo2bgr0r)\\
次に解くのは387. First Unique Character in a String(https://leetcode.com/problems/first-unique-character-in-a-string/?envType=problem-list-v2&envId=xo2bgr0r)

## Step 1
先頭から順番に各要素について後ろにある各要素を足してtargetと比較するやり方が一番直感的に思いついたので書いてみる。各要素について線形の走査が入るので時間計算量がO(n^2)になる。想定解法ではないが一回書いてみる。
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer = [i, j]
                    break
        return answer
```
## Step 2
先頭の要素から順番に、targetとの差分を計算して、その差分の値がそれより前にあればそのindexを持ってくるやり方であれば、1回の走査とハッシュマップへのアクセスだけで済むので、時間計算量はO(n)になる。一方でハッシュマップを置いておくメモリが必要で、そのメモリはnumsの要素数に対して比例になるため、空間計算量もO(n)になる。
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in visited:
                answer = [visited[diff], i]
                break
            else:
                visited[nums[i]] = i
        return answer

```