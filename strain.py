from node import Node

class Strain:
    def __init__(self, data):
        self.root = Node(data)

    def find_node(self, path):
        node = self.root
        for i in path:
            node = node[i]
        return node

    def remove_node(self, path):
        return self.find_node(path).parent.remove(path[-1])

    def splice(self, source, target):
        target_node = self.find_node(target[:-1])
        node = self.remove_node(source)
        target_node.add(target[-1], node)
        if node.find_root() != self.root:
            raise ValueError('Illegal splice.')
        if not self.is_legal():
            raise ValueError('Illegal splice.')

    def available_spots(self):
        return self.root.available_spots()

    def is_legal(self):
        return self.root.is_legal()

    def as_tuple(self):
        return self.root.as_tuple()
