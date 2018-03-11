#makes use of imperative programming
#handles data and methods on those data

class Kettle(object):
    
    power_source = "electricity"
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.on = False
        
    def switch_on(self):
        self.on = True

kenwood = Kettle("Kenwood", 8.99)
braun = Kettle("Braun", 15.79)

print (kenwood.price)
print (braun.name)

braun.price = 98.00

print (braun.price)

print ("Models: {0} = {3}, {2} = {1}".format(kenwood.name,kenwood.price,braun.name, braun.price))
print("Models: {0.name} = {0.price}, {1.name} = {1.price}".format(kenwood, braun))

print(kenwood.on)
kenwood.switch_on()
print(kenwood.on)


print ("*" * 40)
kenwood.power = 1.5
print (kenwood.power)
Kettle.power_source = "atomic"

kenwood.power_source = "gas"
braun.power_source = "electricity"
print (Kettle.power_source)
print (kenwood.power_source)
print (braun.power_source)

#create new instance of Kettle
hamilton = Kettle("Hamilton", 9.99)
print (hamilton.power_source, hamilton.name)
# print (Kettle.__dict__)
# print (kenwood.__dict__)
