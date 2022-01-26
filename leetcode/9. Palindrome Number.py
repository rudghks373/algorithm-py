class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        strX = str(x)
        temp = ''
        for  i in range(len(strX)-1, -1 ,-1):
            temp += strX[i]
        if strX == temp:
            return True
        else:
            return False
    
    # 문자열 슬라이싱을 이용하는 방법
    def isPalindrome2(self, x: int) -> bool:
        temp = str(x)
        return True if temp == temp[::-1] else False
        
