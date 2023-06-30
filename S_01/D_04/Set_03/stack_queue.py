from queue import Queue


class Stack:
    def __init__(self):
        self.queue = Queue()

    def push(self, value):
        self.queue.put(value)

    def pop(self):
        if self.queue.empty():
            return None

        # Move all elements except the last one to the end of the queue
        for _ in range(self.queue.qsize() - 1):
            self.queue.put(self.queue.get())

        # Return the last element (simulating stack behavior)
        return self.queue.get()


# Example usage
stack = Stack()
output = []

stack.push(1)
stack.push(2)
output.append(str(stack.pop()))

stack.push(3)
output.append(str(stack.pop()))
output.append(str(stack.pop()))

output.extend([str(stack.pop()), str(stack.pop())])

output_str = ", ".join(output)
print(output_str)
