print('Task 1')


def is_admin(func):
    def wrapper(*agrs, **kwargs):
        if kwargs['user_type'] != 'admin':
            raise ValueError('ValueError: Permission denied')
        func(*agrs, **kwargs)

    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    print('# Some very dangerous operation')


try:
    show_customer_receipt(user_type='admin')
except Exception:
    pass


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
        count_result = 0
        annot = func.__annotations__
        for i, v in enumerate(args):
            agr_name = list(annot)[i]
            if type(v) != annot[agr_name]:
                print(f'{agr_name} should be a {annot[agr_name]}')
                count_result += 1
        if count_result == 0:
            fucn_res = func(*args)
            if type(fucn_res) == annot['return']:
                print(fucn_res)
            else:
                print(int(fucn_res))
    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


add(5, 4)

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
