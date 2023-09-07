import time

class LeakyBucket:

    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.water = 0
        self.last_time = time.time()


    def fill(self, amount):
        now = time.time()
        elapsed = now - self.last_time
        self.water -= self.leak_rate * elapsed
        self.water = max(self.water, 0)

        if self.water + amount < self.capacity:
            self.water += amount
            self.last_time = now
            return True
        else:
            self.last_time = now
            return False
        
    def get_remaining_space(self):
        return self.capacity - self.water
    


# Capacity of 10 units and leak rate of 1 unit/second
bucket = LeakyBucket(10, 1) 


if bucket.fill(51):
    print("Added 5 units of water.")
else:
    print("Bucket overflow!")

time.sleep(3)  # Simulate a wait time

if bucket.fill(5):
    print("Added 5 units of water.")
else:
    print("Bucket overflow!")

print(f"Remaining space in bucket: {bucket.get_remaining_space()} units")  
        
