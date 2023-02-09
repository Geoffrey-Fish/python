class Data:
    def __init__(self,limit):
        self.limit = limit
    
    def __iter__(self):
        self.value = 10
        return self
    
    def __next__(self):
        x = self.value
        if x > self.limit:
            raise StopIteration
        else:
            self.value = x+1
            return x
# I dont really get it. it starts at x, but x is in the first iteration allready 11, or not?
for i in Data(200):
    print(i)
