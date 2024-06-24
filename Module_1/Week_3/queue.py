class MyQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def is_full(self) -> bool:
        return len(self.queue) == self.capacity

    def enqueue(self, value):
        if not self.is_full():
            self.queue.append(value)
        else:
            raise OverflowError("Queue is full")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Front from an empty queue")


if __name__ == "__main__":
    queue1 = MyQueue(capacity=5)

    queue1.enqueue(1)
    queue1.enqueue(2)

    assert not queue1.is_full(), "Queue should not be full"
    print(queue1.is_full())  # Output: False

    assert queue1.front() == 1, f"Expected front element to be 1, but got {
        queue1.front()}"
    print(queue1.front())  # Output: 1

    assert queue1.dequeue() == 1, f"Expected dequeued element to be 1, but got {
        queue1.dequeue()}"
    print(queue1.dequeue())  # Output: 1

    assert queue1.front() == 2, f"Expected front element to be 2, but got {
        queue1.front()}"
    print(queue1.front())  # Output: 2

    assert queue1.dequeue() == 2, f"Expected dequeued element to be 2, but got {
        queue1.dequeue()}"
    print(queue1.dequeue())  # Output: 2

    assert queue1.is_empty(), "Queue should be empty"
    print(queue1.is_empty())  # Output: True
