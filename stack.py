class Stack:
    _items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if len(self._items) > 0:
            return self._items.pop()

    def top(self):
        if len(self._items) > 0:
            return self._items[-1]

    def contains(self, x, y):
        for cell in self._items:
            if cell.x == x and cell.y == y:
                return True
        return False

    def __len__(self):
        return len(self._items)
