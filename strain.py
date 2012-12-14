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

    def add_node(self, path, node):
        parent = self.find_node(path[:-1])
        parent.add(path[-1], node)

    def splice(self, source, target):
        node = self.remove_node(source)
        self.add_node(target, node)

    def as_tuple(self):
        return self.root.as_tuple()
