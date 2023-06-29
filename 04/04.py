def is_prime(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return num != 1


def find_prime(a, b):
    find_prime_list = ''
    for i in range(a, b+1):
        if is_prime(i):
            find_prime_list += str(i) + ' '
    return find_prime_list


print(find_prime(5, 40))


# Task 2
def unique_character(s: str) -> bool:
    for i in s:
        if s.count(i) > 1:
            return False
    return True

print(unique_character("1234567890rtyu"))


# Task 3
def fibonacci(n):
    odd = 0
    even = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            odd += even
        else:
            even += odd
        fibo_n = odd if i % 2 == 0 else even
    return (fibo_n)


print(fibonacci(20))


 # Task 4
def my_swapcase(input_string: str) -> str:
    swap_input_string = ''
    for i in input_string:
        i = i.upper() if i.islower() else i.lower()
        swap_input_string += i
    return swap_input_string

print(my_swapcase('HelLo!'))


 # Task 5
def simple_interest(initial_amount, interest_rate, years):
    for i in range(years):
        initial_amount += initial_amount*interest_rate
    return ('%.2f' % initial_amount)

print(simple_interest(10000, 0.1, 10))


# Task 6
def password_strength(password):
    length = len(password)
    low_let = 0
    upp_let = 0
    digits = 0
    spec_char = 0
    spec_char_str = '!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~ '
    password = ''.join(set(password))
    for i in password:
        low_let += 1 if (i.isalpha() and i.islower()) else 0
        upp_let += 1 if i.isupper() else 0
        digits += 1 if i.isdigit() else 0
        spec_char += 1 if i in spec_char_str else 0
        password = password.replace(i, '')
    total = length + low_let * 2 + upp_let * 3 + digits * 4 + spec_char * 5
    str_low_let = f' + {low_let} * 2 for lowercase letter' if low_let > 0 else ''
    str_upp_let = f' + {upp_let} * 3 for each uppercase letter' if upp_let > 0 else ''
    str_digits = f' + {digits} * 4 for each digit' if digits > 0 else ''
    str_spec_char = f' + {spec_char} * 5 for each special character' if spec_char > 0 else ''
    return (f'{total} # {length} for each symbol' + str_low_let + str_upp_let + str_digits + str_spec_char)


print(password_strength('abc 123b3'))

# Task 7
def encrypt(message, n):
    plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypt_message = ''
    for i in message:
        if i in plain:
            if (plain.find(i) + n ) <= 25:
                i = plain[int(plain.find(i)) + n ]
            else:
                i = plain[-26 + int(plain.find(i)) + n ]
        encrypt_message += i
    return encrypt_message

def decrypt(message, n):
    plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypt_message = ''
    for i in message:
        if i in plain:
            i = plain[int(plain.find(i)) - n ]
        decrypt_message += i
    return decrypt_message


print(encrypt('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 3))
print(decrypt(encrypt('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 3), 3))
