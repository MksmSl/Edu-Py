print('Tast 1')
def input_int():
    a = input('Please input an intenger: ')
    return a
   
    
def intenger_to_int():
    x = input_int()
    try:
        intenger = int(x)
        print(intenger)
    except ValueError:
        print ('It isn\'t an intenger')
        intenger_to_int() 

intenger_to_int()

print('Tast 2')

def input_str_and_int():
    s = input ('Please, input a string: ')
    n = input ('Please, input an intenger n: ')
    return s, n

def print_char_n_in_str():
    s, n = input_str_and_int()
    try:
        print (s[int(n)-1])
    except ValueError:
        print('n isn\'t an intenger ')
        print_char_n_in_str()
    except IndexError:
        print('n should be less than number of charactes of input string')
        print_char_n_in_str()
print_char_n_in_str()


print('Tast 3')

balance = 1000
def transaction(amount: int, type):
    def deposit():
        new_balance = balance + amount
        print(new_balance)

    def withdrawal():
        new_balance = balance - amount
        print(new_balance)
    try:
        float(amount)
    except ValueError or SyntaxError:
        return print('Argument amount shold be a digit')
    
    if type == 'deposit':
        deposit()
    elif type == 'withdrawal':
        withdrawal()
    else: 
        print('Argument type can be either deposit or withdrawal')

transaction(222, 'withdrawal')


print('Tast 4')


import random
def dice_roll():
    return random.randint(1,6)

print(dice_roll())

print('Tast 5')
def  dice_rolls_1000():
    str_1000_dice_rolls = ''
    for i in range(0,1000):
        str_1000_dice_rolls += str(dice_roll())
    print (str_1000_dice_rolls)
    # print (str_1000_dice_rolls.count('1'))
    for i in range (1,7):
        times_i = str_1000_dice_rolls.count(str(i))
        print (f'There are {times_i}th times of {i}')

dice_rolls_1000()

print('Tast 6')


def recieve_input():
    region_n = input('Enter the number of regions: ')
    try: 
        region_n = int(region_n)
    except ValueError:
        print('It shoud be an intenger!')
        recieve_input()
    ratings_by_reg = ()
    for i in range(1, region_n+1):
        i = input(f'Enter a rating for 1st candidate in {i} region: ')
        try: 
            i = int(i)
        except ValueError:
            print('It shoud be an intenger!')
            recieve_input()
        ratings_by_reg += (str(i),)
    return ratings_by_reg


import random 


def simulate_region_election():
    input_data = recieve_input()
    region_election = ()
    for j in input_data:
        region_election_j = ''
        for i in range(0, 10000):
            region_election_j += 'A' if random.randint(1, 100) <= int(j) else 'B'
        region_election += (str(region_election_j.count('A')),) 
    return region_election


def calculate_announce_result():
    region_election = simulate_region_election()
    candidate_region_election = ()
    result = 0
    for i in region_election:
        print(f'Region {region_election.index(i) + 1}: {i} votes for 1st candidate, {10000 - int(i)} votes for 2nd candidate')
        candidate_region_election += ('A',) if int(i) > 5000 else ('B',)
        result += int(i)
    n_ger = len(region_election)
    if candidate_region_election.count('A') >= candidate_region_election.count('B'):
        print(f'Result: 1nd candidate won with {result} votes and {int(result/n_ger)/100}% of all votes')            
    else:
        print(f'Result: 2nd candidate won with {n_ger*10000 - result} votes and {100 - int(result/n_ger)/100}% of all votes') 


calculate_announce_result()