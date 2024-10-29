
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedQ:
    def __init__(self, head=None, tail=None):
        self._head = head
        self._tail = tail

    def __str__(self):
        if self._head is not None:
            s1 = ""
            self._tail = self._head
            while self._tail.next is not None:
                s1 += str(self._tail.data) + ' '
                self._tail = self._tail.next
            s1 += str(self._tail.data)
            return s1
        else:
            return "The queue is empty"

    def enqueue(self, data):
        if self._head is None:
            self._head = Node(data)
            self._tail = self._head
        else:
            self._tail.next = Node(data)
            self._tail = self._tail.next

    def dequeue(self):
        data = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        return data

    def isEmpty(self):
        return self._head is None

    def size(self):
        "Ser till att räkna varje gång tail får ett next-värde"
        if self._head is not None:
            counter = 1
            self._tail = self._head
            while self._tail.next is not None:
                counter += 1
                self._tail = self._tail.next
            return counter
        else:
            return 0

