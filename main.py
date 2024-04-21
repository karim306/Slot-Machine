import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET  =1 

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8,
}
symbol_value = {
    "A" : 6,
    "B" : 4,
    "C" : 3,
    "D" : 2,
}


def  winning(columns , lines , bet , values) :
    winnings = 0 
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns :
            checkedSymbol = column[0]
            if symbol != checkedSymbol :
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1 )
    return winnings, winning_lines

# def winning(columns, lines, bet, values):
#     winnings = 0
#     winning_lines = []
#     for line in range(lines):
#         symbols_on_line = columns[line]
#         if len(set(symbols_on_line)) == 1:
#             symbol = symbols_on_line[0]
#             winnings += values[symbol] * bet
#             winning_lines.append(line + 1)
#     return winnings, winning_lines



def Slot_Machine(rows , cols , symbols):
    all_symbols = []
    for symbol , symbolCount in symbols.items() :
        for _ in range(symbolCount) :
            all_symbols.append(symbol)

    columns = [[],[],[]]
    for _ in range(cols):
        column = []
        currentSymbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)   
        
        for i, val in enumerate(column):
            columns[i].append(val)
    
    return columns



def print_slot_machine_screen(columns):
    for row in range(len(columns[0])):
        for i , col in enumerate(columns):
            if i != len(columns) -1 :
                print(col[row] ,  end=" | ")
            else:
                print(col[row] , end = "")
        
        print()
        

def deposite():
    while True :
        amount = input("How much you want to deposite ?  $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break 
            else:
                print("Amount must be greater than 0")
        else :
            print("Please enter a number")
    return amount


def get_number_of_lines():
    while True :
        lines = input("Enter the number oflines to bet on  (1-" + str(MAX_LINES) +  ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break 
            else:
                print("Enter a valid Number of lines ")
        else :
            print("Please enter a number")
    return lines

def get_bet():
    while True :
        amount = input("How much you want to bet on each Line ?  $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break 
            else:
                print(f"Amount must be between ${MIN_BET} -${MAX_BET}.")
        else :
            print("Please enter a number")

    return amount   

def GameScreen(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        totalBet = bet * lines

        if balance < totalBet:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")
            continue

        print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${totalBet}")
        print(f"Here is now Your final balance: ${balance - totalBet}")

        slots = Slot_Machine(ROWS, COLS, symbol_count)
        print_slot_machine_screen(slots)
        winnings, winning_lines = winning(slots, lines, bet, symbol_value)
        print(f"You won ${winnings}.")
        print("You won on Lines:", *winning_lines)

        return winnings - totalBet


def main():
    balance = deposite()
    while True:
        print(f"Your current balance is ${balance}")
        spin = input("Press enter to play (q to Quit)")
        if spin == 'q':
            break
        else:
            balance += GameScreen(balance)
    print("You left with ${balance}")

main()
