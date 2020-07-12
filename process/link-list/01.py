class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class LList:
    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def empty(self):
        return self.head is None

    def value_at(self, n):
        res = self.head
        for i in range(1, n + 1):
            if res and res.next:
                res = res.next
            else:
                raise IndexError
        return res

    def push_front(self, node):
        node.next = self.head
        self.head = node

    def pop_front(self):
        if not self.head:
            raise IndexError

        self.head = self.head.next

    def push_back(self, node):
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while self.head.next:
                curr = self.head.next
            curr.next = node

    def pop_back(self):
        if not self.head:
            raise IndexError

        if self.head.next is None:
            self.head = None
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None

    def front(self):
        return self.head

    def end(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr

    def insert(self, index, node):
        if not self.head:
            raise IndexError
        curr = None
        for _ in range(index):
            if curr.next:
                curr = curr.next
            else:
                raise IndexError
        if not curr.next:
            raise IndexError
        elif not curr.next.next:
            curr.next = node
        else:
            node.next = curr.next.next
            curr.next = node.next

    def erase(self, index):
        if not self.head:
            raise IndexError
        curr = None
        for _ in range(index):
            if curr.next:
                curr = curr.next
            else:
                raise IndexError
        if not curr.next:
            raise IndexError
        elif not curr.next.next:
            curr.next = None
        else:
            curr.next = curr.next.next

    def reverse(self):
        curr = self.head
        prev = None
        while curr.next:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp


l_list = LList()
l_list.push_front(ListNode("hello", None))
