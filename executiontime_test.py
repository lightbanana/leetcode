import timeit


class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        open_brackets = [None]  # Put None as a sentinel

        for bracket in s:
            if bracket in open_to_close:
                open_brackets.append(bracket)
            else:
                last = open_brackets.pop()

                if not last or bracket != open_to_close[last]:
                    return False

        return len(open_brackets) == 1


solution = Solution()

s = "()" * 5000

total_time = timeit.timeit(
    lambda: solution.isValid(s),
    number = 1
)

print(f"入力文字数: {len(s):,}")
print(f"合計実行時間: {total_time * 1_000_000:.3f} us")