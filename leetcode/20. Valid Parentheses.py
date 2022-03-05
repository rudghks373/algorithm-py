class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        if s[0] == '(' or s[0] == '{' or s[0] == '[':
            stack.append(s[0])
        else:
            return False
        for index in range(len(s)-1):
            post = s[index+1]
            if stack:
                prefix = stack[-1]
                if (prefix =='(' and post == ')') or (prefix =='{' and post == '}') or (prefix =='[' and post == ']'):
                    stack.pop()
                else:
                    stack.append(s[index+1])
            else:
                stack.append(s[index+1])
        if not stack:
            return True
        else:
            return False
