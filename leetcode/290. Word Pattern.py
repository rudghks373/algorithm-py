class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        input = s.split()
        if len(input) != len(pattern):
            return False
        dic = {}
        for i in range(len(pattern)):
            dic[input[i]] = pattern[i]
        values = {val: key for key, val in dic.items()}
        result = {val: key for key, val in values.items()}
        temp = ''
        for j in range(len(input)):
            temp += str(result.get(input[j]))
        if  temp == pattern:
            return True
        else:
            return False          
