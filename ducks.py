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
    
    def __init__(self):
        self.fly = self.aviate
    def walk(self):
        print ("Waddle waddle I waddle too")
        
    def swim(self):
        print ("Come on in but it's a bit chilly this far south")
        
    def quack(self):
        print ("Are you having a laugh on a penguin?")
        
    def aviate(self):
        print ("I won the lottery and bought a learjet")
class Flock(object):
    
    def __init__(self):
        self.flock = []
        
    def add_duck(self,duck: Duck) -> None:
        fly_method = getattr(duck, "fly", None)
        #if isinstance(duck,Duck):
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("cannot add duck, are you sure it is not a " + str(type(duck).__name__) + "?")
    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing exception handling in migrate") #TODO remove exception before release
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