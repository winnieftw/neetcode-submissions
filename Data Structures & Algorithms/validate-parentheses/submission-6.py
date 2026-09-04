class Solution:
    def isValid(self, s: str) -> bool:
        # symbols = {"{" : "}",
        # "(" : ")",
        # "[" : "]"
        # }

        symbols = {"}":"{",
        ")":"(",
        "]":"["
        }

        if len(s) is None or len(s) % 2 != 0:
            return False

        stack = []
        # val = False
        # other cases: ()[]{}
        for index, c in enumerate(s):
            if c not in symbols:
                stack.append(c)
            elif len(stack) > 0:
                s_pop = stack.pop()
                if s_pop != symbols[c]:
                    return False
            else:
                #return false if stack is empty but "s" length is not
                #example case:  (){}}{
                            #       ^
                            #       |
                return False
        
        #return based off whether the stack is empty or not
        return len(stack) == 0