#8/10/26
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        value = 0
        stack = [] #store each ints that are encountered

        '''
        idea: as you go through each index of the list, store the values in the stack. 
        Once reach operation symbol, pop both values from stack and continue operation. Then 
        add value back to the stack after computation
        '''
        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            # if token.isdigit() or int(token) < 0:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                # #if stack has two values
                # if len(stack) == 2:
                    v2 = int(stack.pop()) #second value in operation
                    v1 = int(stack.pop()) #first value in operation
                    if token == "+":
                        value = v1 + v2
                    elif token == "-":   
                        value = v1 - v2                 
                    elif token == "/":
                        value = v1 / v2
                        value = int(value)
                    elif token == "*":
                        value = v1 * v2
                    
                    stack.append(value)
        return value
                