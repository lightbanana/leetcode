## Step 1
先頭から順に走査していく。その要素以前にあった要素を置いておくdict型変数seenchar_to_indexを用意しておいて,順次追加していく。1回しか出てきていない文字とそのindexを保存しておくdict型変数candidate_to_indexを用意しておいて,今見ている要素がseenchar_to_indexのなかになければ,candidate_to_indexに加える。あったら,candidate_to_indexから外す。最後まで走査したとき,candidate_to_indexが空であれば-1を出力する。そうでなければ,一番最初のcandidate_to_indexの一番最初の要素のvalueを返す。\\
時間計算量はO(n),空間計算量はO(1)

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seenchar_to_index = {}
        candidate_to_index = {}
        for i, char in enumerate(s):
            if char in seenchar_to_index:
                candidate_to_index.pop(char, None)
            else:
                seenchar_to_index[char] = i
                candidate_to_index[char] = i
        if not candidate_to_index:
            return -1
        else:
            return list(candidate_to_index.items())[0][1]
```
## Step 2
### 読んだコード
- https://github.com/attractal/leetcode/pull/19

###　感想
- 一度見た文字を保持するのはdict型変数じゃなくて、set型変数でいい
- dict型変数が追加順を保持するようになったのはPython3.7以降のためOrderedDict(dictのサブクラス)を使うのが無難
- charはc言語の型名などとかぶるので、c(この程度のスコープなら許容か？)やcharacterを使う
- Counterというオブジェクト(dictのサブクラス)は、イテラブルなデータを引数として渡すと、キーが要素、値が出現回数となるdictを返してくれる。(https://docs.python.org/ja/3/library/collections.html#collections.Counter)ので、これを使う。時間計算量O(n), 空間計算量O(n)
- どうせ最初の値しか必要じゃないのに丸ごとlistにするのはメモリの無駄遣いなので、next(iter())を使う?
- popの第2引数がNoneなのはすこし雑な処理に見えるので、dictの中にあるかどうかを先に確認する？

###　解答
解答1:OrderedDictを使う
```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seenchar = set()
        char_to_index = OrderedDict()
        for i, c in enumerate(s):
            if c in seenchar:
                if c in char_to_index:
                    char_to_index.pop(c)
            else:
                seenchar.add(c)
                char_to_index[c] = i
        if not char_to_index:
            return -1
        else:
            return next(iter(char_to_index.values()))
```

解答2:Counterを使う

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_frequency = Counter(s)
        for i, c in enumerate(s):
            if char_to_frequency[c] == 1:
                return i
        return -1
```

- 1がマジックナンバーのように見えるので、only_in_stringなどで置き換える？