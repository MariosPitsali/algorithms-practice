import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a citrus, orange, yummy fruit"
    fruit['lemon'] = "a yellow, sour, citrus fruit"
    fruit["grape"] = "a yum fruit growing in bunches"
    
    print (fruit["lemon"])
    print (fruit["grape"])
