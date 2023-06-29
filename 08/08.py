def rounds_cats_in_hats(n_cats, rounds):
    cats = []
    for i in range(n_cats + 1):
        cats.append(False)
    for i in range(1, rounds + 1):
        for j in range(1, n_cats//i+1):
            cats[j*i] = False if cats[j*i] == True else True
    for i in range(1, n_cats + 1):
        if cats[i] == True:
            print(i, ' ', end='')


rounds_cats_in_hats(100, 2)       
    




# # for i in range(100):
# #     print(i)

# # i = 3
# cats = []
# for i in range(100):
#     cats.append(False)
# # print(cats)
# # print(cats[99])

# n_rounds = 50
# # def round_for_cats(i: int, cat_list: list) -> list:
# for i in range(1, n_rounds+1):
#     if i < 50:
#         for j in range(100//i):
#             if j == 0:
#                 cats[0] = True
#             elif cats[j*(i)-1] == True:
#                 cats[j*(i)-1] = False
#             else:
#                 cats[j*(i)-1] = True
#     else:
#         if cats[i-1] == True:
#             cats[i-1] = False
#         else:
#             cats[i-1] = True

# for i in range(100):
#     if cats[i] == True:
#         print (str(i+1))

# # for i in range(1, 101):
# #     if cats[i] == True:
# #         print(1 + '  ')
            
        
    


# # 1 100
# # 2 100/2
# # 3 100%%3