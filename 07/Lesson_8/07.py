import random

print('Task 1')
capitals = {
        'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin',
        'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa',
        'Switzerland': 'Bern', 'Austria': 'Vienna',
        'Belgium': 'Brussels',  'Sweden': 'Stockholm',
        'Norway': 'Oslo', 'Denmark': 'Copenhagen',
        'Finland': 'Helsinki', 'Poland': 'Warsaw',
        'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens',
}
list = list(capitals)
print('For every right answer you get 1 point. You have 5 rounds.')
print('You can quite typing "exit"')
print()
points = 0
for i in range(5):
    country = random.choice(list)
    guess_capital = input(f'Guess the capital of {country}: ')
    if guess_capital == capitals[country]:
        print(f'You are right! It is {guess_capital}')
        points += 1
        print(f'You have {points} points \n')
    elif guess_capital == 'exit':
        break
    else:
        print('You are wrong!')
        print(f'You have {points} points\n')
    continue

print(f'You have {points} points')
print('The game is over!')

print('Task 2')


def roman_to_int(s):
    symbol_value = { 
                'I': 1, 'V': 5, 'X': 10,'L': 50,
                'C': 100, 'D': 500,'M': 1000,       }
    total = 0
    for i, v in enumerate(s):
        if i == len(s)-1:
            total += symbol_value[v]
        elif symbol_value[v] >= symbol_value[s[i+1]]:
            total += symbol_value[v]
        else:
            total += -symbol_value[v]
    return total


def test_roman_to_int():
     result1 = roman_to_int("III")
     assert result1 == 3

     result2 = roman_to_int("LVIII")
     assert result2 == 58
     
     result3 = roman_to_int("MCMXCIV")
     assert result3 == 1994


test_roman_to_int()


print('Task 4')


def majority_element(nums: list) -> int:
    dic_nums = {}
    for i in set(nums):
        dic_nums[nums.count(i)] = i 
    return max(list(dic_nums))


def test_majority_element() -> int:
    result1 = majority_element([3, 2, 3])
    assert result1 == 3

    result1 = majority_element([2, 2, 1, 1, 1, 2, 2])
    assert result1 == 2


print('Task 5')


def get_subjects_not_passed_by_all_students(student_exams):
    set_student_exams = set()
    for i in student_exams:
        if i[1] < 60:
            set_student_exams.add(i[2])
    return set_student_exams


def test_get_subjects_not_passed_by_all_students():
    exams = [
        ("Alice", 85, "Math"),
        ("Bob", 59, "Math"),
        ("Charlie", 65, "Math"),
        ("Alice", 90, "Science"),
        ("Bob", 80, "Science"),
        ("Charlie", 32, "Science"),
        ("Alice", 95, "History"),
        ("Bob", 85, "History"),
        ("Charlie", 90, "History"),
    ]

    assert get_subjects_not_passed_by_all_students(exams) == {"Science", "Math"}


test_get_subjects_not_passed_by_all_students()