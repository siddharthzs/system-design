"""
Design a distributed key value cachine system, like Memcached or Redis.
```````````````````````````````````````````````````````````````````````
App  ---->  Cache ---> Database
App  <----  Cache <--- Database

1) Features
2) Estimation
3) Design Goals

4) Deep Dive


1) Features=>
        Quick Fetch/Search
        Fast Add : Can be compramised
        Capacity : 
        What to do when more entries are there than capacity


   Write Through Cache: write is confirmed when DB and cache both succeed.
                        Useful where application which write and re-read the information quikly.
                        However, Write latency will be higher, as 2 seprate write
  
   Write Around Cache:  write directly goes to database,
                        chache, Reads DB in case of miss
                        Ensures lower write load and faster writes
                        can lead to higher read latency incase of applicatons
    
    Write Back Cache:  write to cache, then write to DB asynchronously
                        Leads to quick write latency & high write thoughput
                        Risk of losing data incase of cachine layer dies.
                        We reduce risk by having more than one replica acknowledging the write

2) Estimation=>
        Scale and Consistency
        QPS we expect? Queries per second = QPS
        QPS is required for computation power needed. no. of machine

3) Design Goals=>
        Latency: Low
        Consistency: High
        Availability: High
        Cost: Available

4) Deep Dive=>
        How cache will work on a single machine with single theread
        Cost/ Space / Speed / Consistency : which is more important

 
"""

class LRUCache:
    mylist = []
    N = 0
    mymap = dict()
    def __init__(self, capacity):
        self.N = capacity

    def get(self, key):
        if(key not in self.mymap):
            return -1
        if(len(self.mylist) == self.N):
            self.mylist.pop(0)
        self.mylist.append(key)
        return self.mymap[key]

    def set(self, key, value):
        if(len(self.mylist) == self.N):
            v = self.mylist.pop(0)
            if(v in self.mymap):
                del self.mymap[v]
        self.mylist.append(key)
        self.mymap[key] = value
        


L = LRUCache(2)

print(L.set(2,1))
print(L.set(1,1))
print(L.set(2,3))
print(L.set(4,1))
print(L.get(1))
print(L.get(2))
