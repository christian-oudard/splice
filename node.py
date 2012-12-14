class Node:
    def __init__(self, data, parent=None):
        self.parent = parent
        if len(data) == 0:
            self.children = []
        else:
            self.children = [Node(c, parent=self) for c in data]

    def __getitem__(self, index):
        return self.children[index]

    def as_tuple(self):
        if len(self.children) == 0:
            return tuple()
        else:
            return tuple(c.as_tuple() for c in self.children)

    def add(self, index, child):
        self.children.insert(index, child)

    def remove(self, index):
        return self.children.pop(index)
