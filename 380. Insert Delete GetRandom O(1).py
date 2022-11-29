import random
class RandomizedSet:

    def __init__(self):
        self.obj=[]
        

    def insert(self, val: int) -> bool:
        if val not in self.obj:
            self.obj.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.obj:
            self.obj.pop(self.obj.index(val))
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.obj)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
