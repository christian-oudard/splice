from node import Node

class Strain:
    def __init__(self, data):
        self.root = Node(data)

    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()

    def find_node(self, path):
        node = self.root
        for i in path:
            node = node[i]
        return node

    def splice(self, source, target):
        self.add_node(target, self.remove_node(source))

    def remove_node(self, path):
        return self.find_node(path).parent.remove(path[-1])

    def add_node(self, path, node):
        parent = self.find_node(path[:-1])
        parent.add(path[-1], node)
        if node.find_root() != self.root:
            raise ValueError('Illegal addition: disconnected subtree.')
        if not self.is_legal():
            raise ValueError('Illegal addition: {}'.format(self.as_tuple()))

    def legal_moves(self):
        spots = self.available_spots()
        for path, node in self.iter_paths():
            if node == self.root:
                continue
            new_strain = self.copy()
            node = new_strain.remove_node(path)
            spots = new_strain.available_spots()
            for spot in spots:
                resulting_strain = new_strain.copy()
                resulting_strain.add_node(spot, node)
                if resulting_strain != self:
                    yield (path, spot), resulting_strain

    def available_spots(self):
        for path, node in self.iter_paths():
            if len(node.children) == 0:
                yield path + [0]
            elif len(node.children) == 1:
                yield path + [0] # Left side.
                yield path + [1] # Right side.
            elif len(node.children) == 2:
                pass # No room to add more children.

    def copy(self):
        return Strain(self.as_tuple())

    def iter_paths(self):
        return self.root.iter_paths()

    def is_legal(self):
        return self.root.is_legal()

    def as_tuple(self):
        return self.root.as_tuple()
