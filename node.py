class Node:
    def __init__(self, data, parent=None):
        self.parent = parent
        self.children = [Node(c, parent=self) for c in data]

    def __getitem__(self, index):
        return self.children[index]

    def iter_paths(self):
        """
        Generate all descendants and the paths to get to them.
        """
        yield [], self
        for i, child in enumerate(self.children):
            for subpath, descendant in child.iter_paths():
                yield [i] + subpath, descendant

    def add(self, index, child):
        self.children.insert(index, child)
        child.parent = self

    def remove(self, index):
        node = self.children.pop(index)
        node.parent = None
        return node

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
