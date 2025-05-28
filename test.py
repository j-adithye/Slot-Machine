import random

vals = ["a","b","c","d"]

slot_machine = [[1,2,3],
                [4,5,6],
                [7,8,9]]
for i in slot_machine:
    for index,val in enumerate(i):
        i[index] = random.choice(vals)
        
for i in slot_machine:
    print(i)