class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def back_track(par='' ,left=0, right=0):
            print(par)
            if len(par) == n * 2:
                ans.append(par)
            if left < n:
                back_track(par + '(',left+1,right)
            if right < left:
                back_track(par + ')',left,right+1)
        back_track()
        return ans
