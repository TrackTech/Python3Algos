class MyHashMap:
# NOT tested
    def get_hash_key_old(self,key):

        n = key%self.size
        while self.keys[n]!=key and self.keys[n]!=-1:
            n = (n+1)%self.size
        return n
    
    def get_hash_key(self,key,keys,size):
        n = key%size
        while keys[n]!=key and keys[n]!=-1:
            n = (n+1)%size
        return n
    
    def resize_map(self):
        new_size = 2 * self.size
        new_keys = [-1 for _ in range(new_size)]
        new_values = [-1 for _ in range(new_size)]
        for i,k in enumerate(self.keys):
            if k==-1:
                continue
            n = self.get_hash_key(k,new_keys,new_size)
            new_keys[n]=k
            new_values[n] = self.values[i]
        self.keys = new_keys
        self.values = new_values
        self.size = new_size
        self.alert_size = self.size * 0.0


    def __init__(self):
        self.size = 100000
        self.keys = [-1 for _ in range(self.size)]
        self.values = [-1 for _ in range(self.size)]
        self.curr_size = 0
        self.alert_size = self.size *0.9
        

    def put(self, key: int, value: int) -> None:
        if len(self.keys)==self.alert_size:
            self.resize_map()
       
        n = self.get_hash_key(key,self.keys,self.size)
        if self.keys[n]!=key:
            self.curr_size+=1
        self.keys[n]=key
        self.values[n]=value


    def get(self, key: int) -> int:
        ret = -1
        n = key%self.size
        while n<self.size and self.keys[n]!=-1 and self.keys[n]!=key:
            n+=1
        if n==self.size or self.keys[n]==-1:
            return -1
        
        return self.values[n]


    def remove(self, key: int) -> None:
        n = key%self.size
        while self.keys[n]!=-1 and self.keys[n]!=key:
            n = (n+1)%self.size
        self.keys[n]=-1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
