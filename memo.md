## 今回解いた問題と次に解く問題
- 今回解いた問題: 141. Linked List Cycle(https://leetcode.com/problems/linked-list-cycle?envType=problem-list-v2&envId=xo2bgr0r)
- 次に解く問題: 20. Valid Parentheses(https://leetcode.com/problems/valid-parentheses?envType=problem-list-v2&envId=xo2bgr0r)
## Step 1
### 考えたこと
- フロイドの循環検出法を見たことがあったが、とりあえず一度訪れたnodeをsetに保持しておいて、毎回確認する方法が確実なので書いてみる。時間計算量はO(n), 空間計算量はsetを用意するのでO(n)
- setの中にclassを入れることができるかわからなかったので、確認した。
- `while True`は停止しないときが怖いので、使いたくないと感じたが、パッとループを回す方法が思いつかなかったので一度書いてみた。
- 
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
### 読んだコード
- https://discord.com/channels/1084280443945353267/1195700948786491403/1195944696665604156
- https://github.com/tk-hirom/Arai60/pull/1
- https://github.com/katayude/yamaguchiLeetCode/pull/1

### 考えたこと
- Listのinの確認は、線形で舐めるのでできる限りsetで確認をしたい。
- `while head`で最初のifの分岐をなくして可読性を上げられる可能性がある。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            else:
                visited.add(head)
                head = head.next
        return False
```

## Step 3(フロイドの循環検出法で書いてみる)
- fast, slowの2つのポインタを用意して、fastは2ノードずつ進む。slowは1ノードずつ進む。fastとslowが同じノードを指していたら、循環が存在する。
- 利点はsetを用意しなくていいので空間計算量がO(1)になること
- 入力が空のケースをどう組み込むかを考えられず、一度間違ったコードを書いてしまった。(fastの初期値をhead.nextにしてしまった。)ポインタを動かしてから同じかどうかを評価すればいい。
- fast.nextがNoneだとfast.next.nextにアクセスできないケースを考えず、`while fast`で評価してしまった。
- 総じて考慮すべき条件が多いので、元のsetのやり方で書きたいと思った。(空間計算量O(n)が許されるなら。)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
```