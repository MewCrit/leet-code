import math

class BloomFilter:
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.bit_array = [0] * m
        self.salts = [str(i) for i in range(k)]  
        # print(self.bit_array)

    def _hash(self, s, salt):
        return (hash(s + salt) % self.m + self.m) % self.m 
    
    def add(self, s):
        for salt in self.salts:
            self.bit_array[self._hash(s, salt)] = 1

    def check(self, s):
        for salt in self.salts:
            if self.bit_array[self._hash(s, salt)] == 0:
                return False
        return True


# bit array size
m = 1000000

# expected number of items
n = 100000

# hash functions
k = math.ceil((m / n) * math.log(2))

print(k)

bloom_filter = BloomFilter(m, k)

bloom_filter.add("Alice")
bloom_filter.add("Bob")

print("Is Alice in the filter?", bloom_filter.check("Alice"))  # Expected: True
print("Is Bob in the filter?", bloom_filter.check("Bob"))      # Expected: True
print("Is Charlie in the filter?", bloom_filter.check("Charlie"))  # Expected: False (or True due to a potential false positive)
