class Node:
    def __init__(self, data, parent=None):
        self.parent = parent
        self.children = [Node(c, parent=self) for c in data]

    def __getitem__(self, index):
        return self.children[index]

    def add(self, index, child):
        self.children.insert(index, child)
        child.parent = self

    def remove(self, index):
        node = self.children.pop(index)
        node.parent = None
        return node

    def available_spots(self):
        if len(self.children) == 0:
            return [[0]]

        if len(self.children) == 1:
            spots = [[0], [1]]
        elif len(self.children) == 2:
            spots = []

        for i, child in enumerate(self.children):
            for s in child.available_spots():
                spots.append([i] + s)

        return spots

    def is_legal(self):
        return (
            len(self.children) <= 2 and
            all(c.is_legal() for c in self.children)
        )

    def as_tuple(self):
        return tuple(c.as_tuple() for c in self.children)

    def find_root(self):
        seen = set()
        node = self
        while node.parent is not None:
            if node in seen:
                raise ValueError('Cyclical ancestry.')
            seen.add(node)
            node = node.parent
        return node
