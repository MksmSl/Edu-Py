print('Task 1')


def is_admin(func):
    def wrapper(**kwargs):
        user_type = kwargs['user_type'] 
        if user_type == 'admin':
            func(user_type)
        else:
            print('ValueError: Permission denied')
    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    print('# Some very dangerous operation')


show_customer_receipt(user_type='admin')


print('Task 2')


def duplicate_exec(func):
    def wrapper(*args):
        try:
            func(*args)
        except KeyError:
            print(f'Found 1 error during execution of your function: \
KeyError no such key as {next(iter(*args))}')
    
    return wrapper


@duplicate_exec
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'keye': 'bar'})


print('Task 3')


def check_types(func):
    def wrapper(*args):
        for i in args:
            if not isinstance(i, int):
                print(f'TypeError: Argument must be int, not {type(i)}')
                return print('Please, enter an int')
        func_result = func(*args)
        if not isinstance(func_result, int):
            print(int(func_result))
        else:
            print(func_result)
    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a / b


add(8, 4)
add('8', [4])
print('Task 4')


cashe = {}
def cash_decor(func):
    def wrapper(arg):
        if arg not in cashe:
            func_result = func(arg)
            cashe[arg] = func_result
            print(func_result)
        else:
            print(f'cashe result {cashe[4]}')
    return wrapper


@cash_decor
def multiple_3(a):
    return a**3


multiple_3(4)
multiple_3(4)