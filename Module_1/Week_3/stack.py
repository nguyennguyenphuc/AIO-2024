class MyStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def is_full(self) -> bool:
        return len(self.stack) == self.capacity

    def push(self, value):
        if not self.is_full():
            self.stack.append(value)
        else:
            raise OverflowError("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Top from an empty stack")


if __name__ == "__main__":
    stack1 = MyStack(capacity=5)

    stack1.push(1)
    stack1.push(2)

    assert not stack1.is_full(), "Stack should not be full"
    print(stack1.is_full())  # Output: False

    assert stack1.top() == 2, f"Expected top element to be 2, but got {
        stack1.top()}"
    print(stack1.top())  # Output: 2

    assert stack1.pop() == 2, f"Expected popped element to be 2, but got {
        stack1.pop()}"
    print(stack1.pop())  # Output: 2

    assert stack1.top() == 1, f"Expected top element to be 1, but got {
        stack1.top()}"
    print(stack1.top())  # Output: 1

    assert stack1.pop() == 1, f"Expected popped element to be 1, but got {
        stack1.pop()}"
    print(stack1.pop())  # Output: 1

    assert stack1.is_empty(), "Stack should be empty"
    print(stack1.is_empty())  # Output: True
