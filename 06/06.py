print ('Task 1')
def compute_difference(first: list, second: list) -> tuple:
    new_1 = first[:]
    new_2 = second[:]
    for i in first:
        if i in new_2:
            new_1.remove(i)
            new_2.remove(i)
    return new_1, new_2

def compute_difference(first: list, second: list) -> tuple:
    new_1 = first[:]
    new_2 = second[:]
    [(new_2.remove(i), new_1.remove(i)) for i in first if i in new_2]
    return new_1, new_2

def test_compute_difference():

    result1 = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b', 'c'], ['e'])
    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])
    result3 = compute_difference([1, 2, 3], [4, 4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 4, 5, 6])
    result4 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result4 == ([1], [4])


test_compute_difference()


print ('Task 2')


def sum_of_two(nums: list, traget: int) -> list:
    for count, value in enumerate(nums):
        for count_i, value_i in enumerate(nums):
            if (value + value_i == traget) and (count < count_i):
                return [count, count_i]


def test_sum_of_two():
    result1 = sum_of_two([2,7,11,15], 9)
    assert result1 == [0, 1]
    result2 = sum_of_two([3,2,4], 6)
    assert result2 == [1, 2]
    result3 = sum_of_two([3,3], 6)
    assert result3 == [0, 1]


test_sum_of_two()


print ('Task 3')


def unique_elements(arr: list) -> list:
    return [i for i in arr if arr.count(i) == 1]


def test_unique_elements():
    result1 = unique_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]
    result2 = unique_elements([1, 2, 3, 4, 5])
    assert result2 == [1, 2, 3, 4, 5]
    result3 = unique_elements([1, 1, 1, 1, 1])
    assert result3 == []

test_unique_elements()

print ('Task 4')


def odd_elements(arr: list) -> list:
    odd_elements = [v for i, v in enumerate(arr) if arr.count(v) % 2 != 0 and i <= arr.index(v)]
    return odd_elements


def test_odd_elements():
    result1 = odd_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]
    result2 = odd_elements([1, 2, 3, 2, 4, 5, 5, 6, 6, 6])
    assert result2 == [1, 3, 4, 6]


test_odd_elements()


print ('Task 5')


def second_largest_element(arr: list) -> int:
    new_arr = arr[:]
    new_arr.remove(max(new_arr))
    if max(new_arr) > min(new_arr):
        return max(new_arr)

def test_second_largest_element():
    result1 = second_largest_element([1, 2, 3, 2, 4, 5, 5])
    assert result1 == 5
    result2 = second_largest_element([1, 2, 3, 4, 5])
    assert result2 == 4
    result3 = second_largest_element([1, 1, 1, 1, 1])
    assert result3 == None

test_second_largest_element()

print ('Task 6')
cities = [
('New York City', 8550405),
('Los Angeles', 3792621),
('Chicago', 2695598),
('Houston', 2100263),
('Philadelphia', 1526006),
('Phoenix', 1445632),
('San Antonio', 1327407),
('San Diego', 1307402),
('Dallas', 1197816),
('San Jose', 945942),
]
cities.sort(key=lambda a: a[1])
total = 0
for i in cities:
    total += i[1]
print(cities)
print()
print(f'Average population for cities from this list is {total/len(cities)}.')
print(f'Total population for cities from this listis {total}.')
