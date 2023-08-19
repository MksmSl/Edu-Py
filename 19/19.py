import numpy as np
import pandas as pd


print('task 1a')
a = np.zeros((4, 3))
print(a)
b = np.ones((4, 3))
print(b)
c = np.random.randint(0, 11, (4, 3)) 
print(c)

print('task 1b')
ar1 = np.arange(10)
ar2 = 2 * ar1 ** 2 + 5
ar = np.array([ar1, ar2])
print(ar)

print('task 1c')
ar1 = np.arange(-10, 10)
ar2 = np.exp(-ar1)
ar = np.row_stack([ar1, ar2])
print(ar)

print('task3a')

df = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv')
print('task3b')
selected_df = pd.DataFrame(
    df,
    columns=["Team", "Yellow Cards", "Red Cards",]
)
print(selected_df)
print('task3c')
print(f'{len(df)} teams participated in the Euro2012')
print('task3d')
teams_df = pd.DataFrame(
    df,
    columns=["Team", "Goals",]
)

print(teams_df[df.Goals >= 6])
