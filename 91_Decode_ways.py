class Solution: #DP, Time: O(N), Space: O(1)
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        prev, cur = 1, 1
        for i in range(1, len(s)):
            if s[i] != '0':
                tmp = cur
                if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                    tmp += prev
                cur, prev = tmp, cur
            else:
                if s[i-1] == '1' or s[i-1] == '2':
                    cur = prev
                else:
                    return 0
        return cur
