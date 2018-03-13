import random

console_string = "Please choose the dice you want to roll: \n 1) 4d \n 2) 6d \n 3) 8d \n 4) 10d \n 5) 20d \n"
choice = int(input(console_string))
dice = {1: 4, 2:6, 3: 8, 4:10, 5:20}
times_output = "How many times do you want to roll? "
times = int(input(times_output))

rolls = []
for i in range(times):
    rolls.append(random.randint(1,dice[choice]))
print ("The results: ")
for roll in rolls:
    print (roll)