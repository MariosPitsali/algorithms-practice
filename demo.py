if __name__ == "__main__":
    lst = []
    
    with open("demo.txt", 'r') as demo:
        for line in demo:
            person = tuple(line.split(" "))
            name, surname = person
            lst.append(person)
        for item in lst:
            name, surname = item
            name = "mar"
            print ("%s has surname %s" %(name, surname), end="\t")
    
        with open("write.txt", 'w') as db:
            for item in lst:
                name, surname = item
                print(name, surname, sep="\t", file=db)