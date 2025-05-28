import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

SLOT_ROWS = 3
SLOT_COLS = 3



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

def main():
    wallet = deposit()
    lines = no_of_lines_input()
    bet = get_bet()
    total_bet = bet * lines
    if total_bet < wallet:
        print(f"Betting ${bet} on {lines} lines. Total bet is ${total_bet}")
    else:
        print("Not enough Balance")
        print(f"Balance : {wallet} Lines : {lines} " )
    
if __name__ == "__main__":
    main()