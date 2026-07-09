## 今回解いた問題と次に解く問題
- 今回解いた問題:20. Valid Parentheses(https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=xo2bgr0r)
- 次に解く問題:703. Kth Largest Element in a Stream(https://leetcode.com/problems/kth-largest-element-in-a-stream/?envType=problem-list-v2&envId=xo2bgr0r)

## Step 1
### 考えたこと
スタックに([{が来るたびに一つずつ積んでいって、)]}が来るたびに一つずつスタックからpopしていく。スタックの名前がスタックなのは少し嫌だと思ったが、他に思いつかなかったのでとりあえずstackにした。時間計算量はO(n)、空間計算量もO(n)。
分岐が多くて読みづらいので、もう少し読みやすく書けないかと思った。

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not s:
            return True
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c == ")":
                if not stack:
                    return False
                last = stack.pop()
                if last == "(":
                    continue
                else:
                    return False
            elif c == "]":
                if not stack:
                    return False
                last = stack.pop()
                if last == "[":
                    continue
                else:
                    return False
            elif c == "}":
                if not stack:
                    return False
                last = stack.pop()
                if last == "{":
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False
```
## Step 2
### 読んだコード
- https://github.com/bumbuboon/Leetcode/pull/7/changes
- https://github.com/philip82148/leetcode-swejp/pull/11/changes

### 考えたこと
- 先に[と]みたいにペアを作っておく。open_to_closeのような名前のdictionary型変数がいいか。
- return(len(stack) == 0)だと可読性が高い
- スタックの名前がstackの代わりの名前として、open_bracketsなどがある。
- if not stackの分岐を避けるためにあらかじめstackの中に番兵(Cだと\0などの目印、PythonだとNoneなどか?(->Noneだとdictにアクセスできないので#など))を入れておくのも有効。

```python
class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = []
        open_to_close = {'(' : ')',
                         '{' : '}',
                         '[' : ']'}
        for c in s:
            if c in open_to_close:
                open_brackets.append(c)
            elif not open_brackets:
                return False
            else:
                last = open_brackets.pop()
                if open_to_close[last] != c:
                    return False
        return (len(open_brackets) == 0)
```
## Step 3
- 番兵を使って書いてみる。dictへのアクセスは結局その中にキーがあるかを確認する必要があるので、分岐の数自体は変わらないが、分岐より先にpopできるのが直感的でわかりやすい。

```python
class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {'(' : ')',
                         '{' : '}',
                         '[' : ']'}
        open_brackets = [None] # Put None as a sentinel
        for bracket in s:
            if bracket in open_to_close:
                open_brackets.append(bracket)
            else:
                last = open_brackets.pop()
                if not last or bracket != open_to_close[last]:
                    return False
        return (len(open_brackets) == 1) # Check only the sentinel left 
```
