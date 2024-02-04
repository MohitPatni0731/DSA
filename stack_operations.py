q = int(input())
queries = []

for i in range(q):
    query = input()
    queries.append(query)
    
class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def push_n_times(self, n, x):
        self.stack.extend([x] * n)
        
    def pop_and_print(self):
        if self.stack:
            print(self.stack.pop())
        else:
            print("Stack is empty")
            
    def pop_n_and_print_sum(self, n):
        sum_popped = 0
        for _ in range(min(n, len(self.stack))):
            sum_popped += self.stack.pop()
        print(sum_popped)

    def print_sum(self):
        print(sum(self.stack))

def process_queries(queries):
    custom_stack = Stack()
    for query in queries:
        if query[0] == 1:
            custom_stack.push(query[1])
        elif query[0] == 2:
            custom_stack.push_n_times(query[1], query[2])
        elif query[0] == 3:
            custom_stack.pop_and_print()
        elif query[0] == 4:
            custom_stack.pop_n_and_print_sum(query[1])
        elif query[0] == 5:
            custom_stack.print_sum()

