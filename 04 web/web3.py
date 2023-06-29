def bal_paranthesis(s):
    total = 0
    for i in s:
        total += 1 if i == '(' else -1
        if total < 0:
            return False
        break
    bal = True if total == 0 else False
    return bal


print (bal_paranthesis('())'))
