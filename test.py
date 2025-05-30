import random

def calc_result(s_m):
    valid_lines = 0
    
    for row in range(3):
        last_row = s_m[-1]
        first_row = s_m[0]
        val = first_row[row]
        for col in range(3):
            # print("index ",row," ",col)
            # print("val : ",val)
            # print("curr",s_m[col][row])
            if s_m[col][row] != val:
                break
            elif val == s_m[col][row] and col == 2:
                valid_lines += 1
    return valid_lines

vals = ["a","b","c","d"]

slot_machine = [[1,2,3],
                [1,2,3],
                [1,2,3]]
# for i in slot_machine:
#     for index,val in enumerate(i):
#         i[index] = random.choice(vals)
        
for i in slot_machine:
    print(i)
    
v = calc_result(slot_machine)
print(v)