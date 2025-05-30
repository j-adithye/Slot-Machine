import random

MAX_LINES = 7
MAX_BET = 100000
MIN_BET = 10



def run_slot_machine():
    #generate slot machine
    symbols = [ 'A' , 'B' , 'C' , 'D' , 'E' ]
    slot_machine = [[random.choice(symbols) for _ in range(MAX_LINES)] for _ in range(MAX_LINES)]
    return slot_machine

def deposit():
    while True:
        amount = input("Enter your Deposit amount $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("enter amount greater than 0")
        else:
            print("enter a number")
    return amount

def no_of_lines_input():
    # How many lines are you betting
    while True:
        lines = input("Enter no of lines (1-"+ str(MAX_LINES) +"): ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print("enter num of lines in given range")
        else:
            print("enter a number")
    return lines

def get_bet():
    while True:
        amount = input("Enter your bet amount $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"enter amount between ${MIN_BET} and ${MAX_BET}")
        else:
            print("enter a number")
    return amount

def calc_result(s_m):
    #Calculate result
    valid_lines = 0
    
    # Horizontal Check
    for row in s_m:
        val = row[0]
        for index,i in enumerate(row):
            if i != val:
                break
            else:
                if index == MAX_LINES-1:
                    valid_lines += 1
    
    #Vertical_check
    for row in range(MAX_LINES):
        last_row = s_m[-1]
        first_row = s_m[0]
        val = first_row[row]
        for col in range(MAX_LINES):
            if s_m[col][row] != val:
                break
            elif val == s_m[col][row] and col == MAX_LINES - 1:
                valid_lines += 1
                    
                    
    return valid_lines
        

def main():
    wallet = deposit()
    
    while wallet>0:
        
        lines = no_of_lines_input()
        bet = get_bet()
        total_bet = bet * lines
    
        if total_bet < wallet:
            print(f"Betting ${bet} on {lines} lines. Total bet is ${total_bet}")
        else:
            print(f"Not enough Balance Your balance is {wallet}")
            break

        wallet = wallet - total_bet
        print(f"Balance : {wallet} || Lines : {lines} || Total Bet : {total_bet}")
    
        print()
        slot_machine = run_slot_machine()
        print("Slot Machine Result:")
        for row in slot_machine:
            for col in range(MAX_LINES):
                print(f"| {row[col]} |",end = '')
            print()
        
        result = calc_result(slot_machine)
        print(f"You won {result} lines")
        
        wallet = wallet + result * bet * 2
        print(f"Updated Balance is {wallet}")
        
        proceed = input("Do you want to continue Y/n (Default value is 'n'):")
        if proceed.lower() == "y":
            print(proceed)
            continue
        else:
            print("Exiting...")
            break
    
    if wallet < 1:
        print("Low Balance")    
    
if __name__ == "__main__":
    main()