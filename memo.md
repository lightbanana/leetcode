## 今回解いた問題と次に解く問題
- 今回解いた問題:703.-Kth-Largest-Element-in-a-Stream(https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- 次に解く問題:283. Move Zeroes(https://leetcode.com/problems/move-zeroes/)

## Step 1
### 考えたこと
- __init__とメソッドで分かれている問題を初めて解くので、PythonのClassについてドキュメントを確認した。(https://docs.python.org/3.14/reference/datamodel.html#object.__new__)
- addメソッドが何回も呼ばれるのに対し、__init__メソッドはインスタンスを生成する最初の一回しか呼ばれない。
- まずは愚直にaddが呼ばれるたびにリストに加えてsortする方法で書いてみる。時間計算量はO(nlogn)のため、100s-1msほどか。さらにこのsortを毎回呼び出すと遅そうなので、もっと適切なデータ構造があると感じた。

```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```
## Step 2
### 読んだコード・考えたこと
- https://github.com/h-masder/Arai60/pull/9/changes
- heapを使うことで、O(logn)で値の追加、O(logn)で最小値へのアクセスが可能になるため、ソートのO(nlogn)より時間計算量を削減することができる。
- heapqはheapをlistに表現したもので、heap[i]の子はheap[i*2+1], heap[i*2+2]に格納されている状態。
- heapのデータ構造の理解のためにheapを実装している。自分もheapを使ったことがないため今度やってみる。CPythonでのheapqライブラリは以下(https://github.com/python/cpython/blob/3.14/Lib/heapq.py)
- maxheapは3.14からのため、互換性を意識するためminheapで書く。minheapを使って最大値を根に持ってきたい場合は負の数としてから格納すればいい。

```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while(len(self.nums) > self.k):
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

```
## Step 3
```python

```
