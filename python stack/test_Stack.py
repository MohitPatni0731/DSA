import unittest
from Stacks import Stack

class TestStack(unittest.TestCase):
    
    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())
    
    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(),1)
        
    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(),2)
        self.assertEqual(stack.pop(),1)
        self.assertTrue(stack.is_empty())
        
    def test_peek(self):
        stack = Stack()
        stack.push(3)
        stack.push(2)
        self.assertEqual(stack.peek(),2)
        stack.pop()
        self.assertEqual(stack.peek(),3)
        
    def test_length(self):
        stack = Stack()
        self.assertEqual(stack.length(), 0)
        stack.push(1)
        self.assertEqual(stack.length(), 1)

    def test_str(self):
        stack = Stack()
        self.assertEqual(str(stack), "Stack is empty")
        stack.push(1)
        stack.push(2)
        self.assertEqual(str(stack), "2\n1")
        
if __name__ == "__main__":
    unittest.main()
