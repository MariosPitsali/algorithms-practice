class Wing(object):
    
    def __init__(self, ratio):
        self.ratio = ratio
        
    def fly(self):
        if self.ratio > 1:
            print ("Weee, this is fun!")
        elif self.ratio == 1:
            print ("This is hard work, but I'm flying")
        else:
            print ("I think I'll just walk")


class Duck(object):
    
    def __init__(self):
#         composition example
        self._wing = Wing(1.8)
        
    def walk(self):
        print ("Waddle waddle waddle")
    
    def swim(self):
        print ("Come on in the water is lovely")
        
    def quack(self):
        print ("Quack Quack")

    def fly(self):
        self._wing.fly()

class Mallard(Duck):
    pass
class Penguin(object):
    
    def walk(self):
        print ("Waddle waddle I waddle too")
        
    def swim(self):
        print ("Come on in but it's a bit chilly this far south")
        
    def quack(self):
        print ("Are you having a laugh on a penguin?")
class Flock(object):
    
    def __init__(self):
        self.flock = []
        
    def add_duck(self,duck: Duck) -> None:
        if isinstance(duck,Duck):
            self.flock.append(duck)
    
    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print ("one duck down")
                problem = e
                #raise
        if problem:
            raise problem
def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ =="__main__":
    donald = Duck()
    donald.fly()