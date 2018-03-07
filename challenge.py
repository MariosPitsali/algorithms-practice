with open("cities.txt", 'a') as city_file:
    for i in range(2,13):
        for j in range(1,13):
            print (" %2d times %2d is %2d" %(j, i, i*j), file=city_file)
        print ( "*" * 50, file=city_file)