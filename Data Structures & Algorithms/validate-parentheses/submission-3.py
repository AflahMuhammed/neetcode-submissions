class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i]=='[':
                stack.append('[')
            elif s[i]=='{':
                stack.append('{')
            elif s[i]=='(':
                stack.append('(')
            elif s[i]==")":
                if not stack:
                    return False
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            elif s[i]=="]":
                if not stack:
                    return False
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            elif s[i]=="}":
                if not stack:
                    return False
                if stack[-1]=='{':
                    stack.pop()
                else:
                    return False   
        if len(stack)==0:
            return True
        else:
            return False 
            