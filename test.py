import random

vals = ["a","b","c","d"]

slot_machine = [[0,0,0]
                [0,0,0]
                [0,0,0]]
for i in slot_machine:
    for index,val in enumerate(i):
        i[index] = random.choice(vals)
        
for i in slot_machine:
    print(i)