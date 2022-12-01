#AoC day 1 by DV


#read input file
with open('day1.txt','r') as f:
   l = f.read().splitlines()
   
#two empty list to take in each elf and append to the food list
food = []
elf = []
for i in l:
    if i != '':
        elf.append(int(i))
    else:
        food.append(elf)
        elf = []
food.append(elf)

total_cal = [sum(x) for x in food]

#The most eaten calories is then...
print("Max total calories: "+ str(max(total_cal)) + "\n")

#Sorting the list to get the top 3 elves
total_cal.sort()
print("top three: "+str(total_cal[-3:]) + " Sum: " + str(sum(total_cal[-3:])))