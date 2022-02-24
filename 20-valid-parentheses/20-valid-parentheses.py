class Solution:
    def isValid(self, s: str) -> bool:
        is_true = False
        while len(s):
            is_true = False
            if s[0] in ['}',']',')']:
                return False
            if len(s)%2==1:
                return False
            for i in range(1,len(s)):
                if s[i]==')' and s[i-1]=='(':
                    s = s[:i-1] + s[i+1:]
                    is_true = True
                    break
                if s[i]=='}' and s[i-1]=='{':
                    s = s[:i-1] + s[i+1:]
                    is_true = True
                    break
                if s[i]==']' and s[i-1]=='[':
                    s = s[:i-1] + s[i+1:]
                    is_true = True
                    break
            if is_true == False:
                return False
        return True    
        
            
    