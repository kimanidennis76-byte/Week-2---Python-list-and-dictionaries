# day 1
week_steps = [9200, 7400, 10500, 8800, 6900, 11000, 9600]

target = 8000

for steps in week_steps:
    if steps >= target:
        print("Goal achieved")
    elif steps < target:
        print("Put more effort")

print("Tracked steps",len(week_steps))
   
print(week_steps)
print(week_steps [-1])

if 9200 in week_steps:
    print("Available in the list")
if 3000 not in week_steps:
    print("3000 Not available in the list") 

week_steps [0] = 9000
print("New steps", week_steps)


# fruits
fruits = ["mango","banana", "apple","orange", "grape"]
print("======Fruits=======")

fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.append("pawpaw")
print(fruits)
fruits.remove("mango")
print(fruits)


        
    
    
    
    
