class Solution:
    def isValid(self, s: str) -> bool:
        starters = ['(','{','[']
        closers  = [')','}',']']
        brackets = []
        for bracket in range(len(s)):
            if s[bracket] in starters:
                brackets.append(s[bracket])
            else:
                if bracket==0:
                    return False
                else:
                    if len(brackets)==0:
                        return False
                    else:
                        if closers.index(s[bracket])==starters.index(brackets[-1]):
                            brackets.pop()
                        else:
                            return False
        if brackets:
            return False
        return True            
        