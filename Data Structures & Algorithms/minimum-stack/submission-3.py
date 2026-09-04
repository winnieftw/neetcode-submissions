#8/10/26: design problem. Goal is to have constant time of each operation
class MinStack:

    def __init__(self):
        self.stack = []
        '''
            want to have another stack. This will run in parallel
            with the current stack. This will store the minimum value
            at each index. Ultimately allow to get O(1) time when
            reaching getMin() operation
            
        '''
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            last_val = self.min_stack[-1]
            min_val = min(last_val, val)
            self.min_stack.append(min_val)
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack and self.min_stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # return min(self.stack) <- O(n) operation since its a list
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return null