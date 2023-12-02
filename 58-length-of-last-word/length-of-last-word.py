class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        last_word_len = 0
        while i >= 0 and s[i] != " ":
            last_word_len += 1
            i -= 1
        return last_word_len
        