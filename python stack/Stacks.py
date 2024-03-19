from collections import deque
class Stack:
    def __init__(self) -> None:
        self.container = deque()
    
    def is_empty(self) -> bool: 
        return len(self.container)==0
    
    def length(self) -> int:
        return len(self.container)
    
    def push(self, i) -> None:
        self.container.append(i)        
        
    def pop(self) -> any:
        return self.container.pop()
    
    def peek(self) -> any:
        return self.container[-1]
    
    def __str__(self) -> str:
        if self.is_empty():
            return "Stack is empty"
        else:
            return "\n".join(str(item) for item in reversed(self.container))
            

