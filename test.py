import random

def calc_result(s_m):
    valid_lines = 0
    
    for row in s_m:
        # print("row:",row)
        val = row[0]
        for index,i in enumerate(row):
            # print("i:",i)
            if i != val:
                break
            else:
                if index == 2:
                    valid_lines += 1
            
    return valid_lines

vals = ["a","b","c","d"]

slot_machine = [[0,0,0],
                [1,0,0],
                [1,0,0]]
for i in slot_machine:
    for index,val in enumerate(i):
        i[index] = random.choice(vals)
        
for i in slot_machine:
    print(i)
    
v = calc_result(slot_machine)
print(v)