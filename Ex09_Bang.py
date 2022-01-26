# Два участника p1 и p2 участвуют в дуэли. 
# Напишите функцию whos_first, которая принимает две строки и возвращает имя игрока, 
# который выстрелил первым.
# Если игроки выстрелили одновременно, то вернуть строку "tie".

print('********* Start of programm *********')

def whos_first(p1, p2):
    if p1.find('1')<p2.find('1'):
        return 'p1'
    elif p1.find('1')==p2.find('1'):
        return 'tie'
    elif p1.find('1')>p2.find('1'):
        return 'p2'

menuPoint=1
while menuPoint!='0':

    player1=input('Print SPACES and "1" for 1p\'s shot: ')
    player2=input('Print SPACES and "1" for 2p\'s shot: ')
    
    print(whos_first(player1, player2))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit