import random

#start with empty list 
lists = []

#loop to generate numbers in range from 0 - 20 using the range function.
for num in range(0,20):
    #add/append each number in the range 0 - 20 to the empty list
    lists.append(num)
    #shuffle the list using the random module
    random.shuffle(lists)


for i in lists:
    #print out each iteration of the shuffled list
    print(f"Number: {i}")
    #print out the square of each iteration
    print(f"The square of the {i} is: {i * i}")
    




