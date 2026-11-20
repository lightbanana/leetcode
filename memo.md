## 今回解いた問題と次に解く問題

## Step 1
### 考えたこと

```python
class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        seen = set()
        for email in emails:
            local_domain = email.split("@")
            local = local_domain[0]
            domain = local_domain[1]
            local_duplicate = local.split("+")
            local = local_duplicate[0]
            local = local.replace(".", "")
            email_origin = local + "@" + domain
            if email_origin not in seen:
                seen.add(email_origin)
        return len(seen)
```
## Step 2
```python

```
## Step 3
```python

```
