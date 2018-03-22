class Wing(object):
    
    def __init__(self, ratio):
        self.ratio = ratio
        
    def fly(self):
        if self.ration > 1:
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

class Penguin(object):
    
    def walk(self):
        print ("Waddle waddle I waddle too")
        
    def swim(self):
        print ("Come on in but it's a bit chilly this far south")
        
    def quack(self):
        print ("Are you having a laugh on a penguin?")

def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ =="__main__":
    donald = Duck()
    donald.fly()
#     test_duck(donald)
#     percy = Penguin()
#     test_duck(percy)
    