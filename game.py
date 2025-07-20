import os
import time

def print_data(data):
    os.system('cls')
    print(f'Coins: {data['Coins']}')
    print(f'Resources: {data['Resources']}')
    print(f'Food: {data['Food']}')
    print(f'Research Points: {data['Research Points']}')
    field = data['Field']
    n = len(field)
    for i in range(n):
        s = ' '
        for j in range(n):
            x = field[i][j]
            if x['building'] is None:
                s = s + '* '
            else:
                s = s + x['building'][0] + ' '
        print(s)
    return 


n = int(input('Choose the number of rows and columns in the field, the smaller, the harder. The field should be a square.(eg. of input: 10): '))
field = [[{'building': None, 'level': 0} for i in range(n)] for j in range(n)] 
game = {'Coins': 10, 'Resources': 10, 'Food': 10, 'Research Points': 0, 'Field': field}
#change so the player chooses what to do. Use 'while' loop
while game['Coins'] >= 0:
    #stuff
    123
print('You lost:(')

# for i in range(n):
#     print_data(game)
#     game['Coins'] -= 1
#     game['Resources'] -= 1
#     game['Field'][i][i]['building'] = 'Mine' if i % 2 == 0 else 'Sawmill'
#     time.sleep(2)
# print_data(game)

# def data_init(n):
#     data = list(list(cell))
#     cell = {'building': None, 'level': 0}
#     return data



# data[5][5]['building'] = 'mine'
# data[5][5]['level'] = '0'