import random
import csv
import pandas as pd

print('Task 1')


def files_a_z():
    summary_content = ''
    for i in range(65, 91):
        file_name = chr(i) + '.txt'
        file_content = str(random.randint(1, 100))
        summary_content += file_name + ': ' + file_content + ' '
        with open(file_name, 'w') as file:
            file.write(file_content)
    with open('summary.txt', 'w') as file:
        file.write(summary_content)


files_a_z()

print('Task 2')
with open('10_02_01.txt', 'r', encoding="utf8") as file_1:
    text = file_1.read()
text.upper()
with open('10_02_02.txt', 'w', encoding="utf8") as file_2:
    file_2.write(text.upper())


print('Task 3')
players = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']


def score_players():
    score_list = []
    for i in range(100):
        for j in players:
            score_list.append([j, random.randint(0, 1000)])

    with open('10_03_core_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Player name', 'Score'])
        for score in score_list:
            writer.writerow(score)


score_players()


print('Task 4')


def high_scores_csv(file):
    df = pd.read_csv(file)
    sorted_df = df.sort_values(by=['Score'], ascending=False)
    with open('high_scores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for j in players:
            for index, row in sorted_df.iterrows():
                if j in (row['Player name']):
                    writer.writerow([row['Player name'], row['Score']])
                    break


high_scores_csv('10_03_score_list.csv')
