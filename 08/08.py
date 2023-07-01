# There has to be a cod until str 12 if cats == rounds
def rounds_cats_in_hats(n_cats, rounds):
    iterations = 0
    cats = []
    if n_cats == rounds:
        for i in range(1, int(n_cats**0.5 + 1)):
            cats.append(i**2)
            iterations += 1
        print('List of cats ws a hat:')
        print(cats)
        print(f'Total amount of iterations is {iterations}')
    else:
        for i in range(n_cats + 1):  # list of cats wo hats
            cats.append(False)
            iterations += 1
        for i in range(1, rounds + 1):  # rounds
            iterations += 1
            for j in range(1, n_cats//i+1):  # putting on/off hats only to every numbers round cat
                iterations += 1
                cats[j*i] = False if cats[j*i] is True else True
        print('List of cats ws a hat:')
        for i in range(1, n_cats + 1):  # printing numbers of cats ws a hat
            if cats[i] is True:
                print(i, ' ', end='')
        print()
        print(f'Total amount of iterations is {iterations}')



rounds_cats_in_hats(100, 100)
