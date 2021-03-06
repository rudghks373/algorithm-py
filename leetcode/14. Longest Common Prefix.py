class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = 200
        for word in strs:
            min_length = min(min_length, len(word))
        strs.sort()
        common_prefix, i = "", 0
        first, last = strs[0], strs[-1]
        while i < min_length and first[i] == last[i]:
            common_prefix += strs[0][i]
            i += 1
        return common_prefix

class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result= []
        for x in zip(*strs):
         if len(set(x)) == 1:
            result.append(x[0])
         else:
            break
        return "".join(result)

