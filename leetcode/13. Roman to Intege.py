class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
        output = 0
        cursor = 0
        while cursor<len(s):
            if cursor+1 != len(s) and s[cursor]+s[cursor+1] in symbol:
                output += symbol[s[cursor]+s[cursor+1]]
                cursor += 2
            else:
                output += symbol[s[cursor]]
                cursor += 1
        return output
