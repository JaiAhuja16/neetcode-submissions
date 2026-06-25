class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache: 
    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def add(self, node):
        prev, next = self.head, self.head.next
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.d:
            self.remove(self.d[key])
            self.add(self.d[key])
            return self.d[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        self.d[key] = Node(key, value)
        self.add(self.d[key])
        if len(self.d) > self.cap:
            del self.d[self.tail.prev.key]
            self.remove(self.tail.prev)
