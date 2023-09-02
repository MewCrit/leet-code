import time

class TokenBucket:
    def __init__(self, capacity, fill_rate):
        self.capacity = capacity
        self.fill_rate = fill_rate
        self.tokens = 0
        self.last_time = time.time()

    def consume(self, amount):
        now = time.time()
        elapsed = now - self.last_time
        self.tokens += self.fill_rate * elapsed
        self.tokens = min(self.tokens, self.capacity)
        
        self.last_time = now
        if self.tokens >= amount:
            self.tokens -= amount
            return True
        else:
            return False

bucket = TokenBucket(100, 10)  
if bucket.consume(20):
    print("Processed request costing 20 tokens.")
else:
    print("Not enough tokens to process the request.")
