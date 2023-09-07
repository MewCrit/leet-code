import hashlib


class ConsistentHashing:

    def __init__(self, nodes=None, replicas=5):
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []

        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        for i in range(self.replicas):
            key = self.hash(f"{node}:{i}")
            self.ring[key] = node
            self.sorted_keys.append(key)
        
        self.sorted_keys.sort()

    def get_node(self, key):
        hash_key = self.hash(key)
        idx = self._get_index(hash_key)
    
        return self.ring[self.sorted_keys[idx]]
    
    def _get_index(self, hash_key):
        for i, key in enumerate(self.sorted_keys):
            if hash_key <= key:
                return i
        return 0
    
    @staticmethod
    def hash(key):
        m = hashlib.sha256()
        m.update(key.encode('utf-8'))
        return int(m.hexdigest(), 16)



ch = ConsistentHashing(["node1", "node2", "node3"])


print(ch.get_node("apple"))
print(ch.get_node("ssss"))


ch.add_node('node 4')

print(ch.get_node("ssss")) 