class Solution: #DP Time: O(N), Space: O(1)
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        elif s[0] == '*':
            prev, cur = 1, 9
        else:
            prev, cur = 1, 1

        for i in range(1, len(s)):
            if s[i] != '0':
                if s[i] == '*':
                    tmp = cur * 9
                    if s[i-1] == '*':
                        tmp += prev * 15
                    else:
                        if s[i-1] == '1':
                            tmp += prev * 9
                        elif s[i-1] == '2':
                            tmp += prev * 6
                else:
                    tmp = cur
                    if s[i-1] == '*':
                        if int(s[i]) <= 6:
                            tmp += prev * 2
                        else:
                            tmp += prev
                    else:
                        if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                            tmp += prev
                cur, prev = tmp, cur
            else:
                if s[i-1] == '*':
                    cur = prev*2
                elif s[i-1] == '1' or s[i-1] == '2':
                    cur = prev
                else:
                    return 0
        return cur % (10**9 + 7)
