## 今回解いた問題と次に解く問題
- 今回解いた問題:392. Is Subsequence https://leetcode.com/problems/is-subsequence?envType=problem-list-v2&envId=xo2bgr0r
- 次に解く問題:141. Linked List Cycle https://leetcode.com/problems/linked-list-cycle?envType=problem-list-v2&envId=xo2bgr0r

## Step 1
### 方針
部分文字列sのどの文字をチェックしているか確かめる変数indexを用意して、チェックされる対象のtの前の数字からs[index]と同じかどうかを確かめていく。同じだった場合、indexを1つ後ろにずらして続ける。sの一番後ろの文字について、同じものが見つかったらその時点でTrueを返す。見つからなかったらFalseを返す。時間計算量はO(n)、空間計算量はO(1)。

### 考えたこと
- sが""だったときはTrueを返すべきなのに、s[0]でアクセスできずエラーになるのでsの長さが0の場合はTrueを返すような処理を加えた。""が入力される場合をあらかじめ考慮すべきであった。
- indexは変数の名前として適切ではない気がしたが、ほかに何か適切な名前が思い浮かばなかった。

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        if len(s) == 0:
            return True
        for i in range(len(t)):
            if s[index] == t[i]:
                index += 1
                if index == len(s):
                    return True
        return False
```
## Step 2
### 読んだコード
- https://github.com/tom4649/Coding/pull/52/changes
- https://github.com/dxxsxsxkx/leetcode/pull/57/changes
### 考えたこと
- indexはs_indexやt_indexなどと書き換えることができる。
- sが空な判定に加えて、tが空かどうかの判定も加えたほうがいい。
- 正規表現で書くやり方もある。この場合、reというモジュールを使う(https://docs.python.org/ja/3/library/re.html)。matchはstringの前方の正規表現がpatternと一致した場合にMatchオブジェクトを返し、一致しなかった場合はNoneを返す関数。文字列の結合の時間計算量はO(n^2)だが、sが小さいので許容範囲か。

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        s_index = 0
        for i in range(len(t)):
            if s[s_index] == t[i]:
                s_index += 1
                if s_index == len(s):
                    return True
        return False
```
## Step 3(正規表現で書く)

```python
import re

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pattern = ""
        for c in s:
            pattern += ".*" + c
        Match = re.match(pattern, t)
        return Match is not None
```