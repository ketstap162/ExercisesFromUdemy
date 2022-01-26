# А теперь первое серьёзное домашнее задание. Вы попробуете разработать игру.
# Предлагаю древнюю китайскую игру в палочки.
# Играют два игрока.  Есть 10 палочек. Игроки по очереди берут от одной до трёх палочек. 
# Играют до тех пор пока не закончатся палочки. Тот кто взял последним - тот проиграл.
# Реализуйте игру таким образом, чтобы могли играть два человека. Изначально есть 10 палочек. 
# На каждом ходу выводите на консоль текущее количество оставшихся палочек и 
# просите ввести количество палочек,которое хочет взять игрок (который делает ход). 
# Не забывайте менять очерёдность игроков и сокращать кол-во палочек. 
# В конце надо вывести кто победил - первый или второй игрок.
# Нюансы реализации могут отличаться. Кто-то может захотет запросить имена у игроков. 
# Кто-то может захотеть реализовать не с 10-ю палочками, а с тем количеством, 
# которое введёт пользователь (может он хочет играть с 20-ю палочками?).

print('\n********* Start of programm *********\n')

menuPoint=1
while menuPoint!='0':

    st_count=int(input('Enter count of sticks:\n'))
    turn=1
    st_turn=0
    while (st_count>0):
        print(f'---------- Turn {turn} ----------')
        print(f'Now you have {st_count} sticks')

        st_turn=int(input('Player 1: Choosing number of stick (1-3):\n'))
        while(st_turn>3 or st_turn<1):
            st_turn=int(input('Wrong number. Player 1, enter number from 1 to 3:\n'))
        st_count-=st_turn
        if st_count<=0:
            print('++++++ Oh, Player 1 lost. Winner - Player 2 ++++++')
            break
        
        st_turn=int(input('Player 2: Choosing number of stick (1-3):\n'))
        while(st_turn>3 or st_turn<1):
            st_turn=int(input('Wrong number. Player 2, enter number from 1 to 3:\n'))
        st_count-=st_turn
        if st_count<=0:
            print('++++++ Oh, Player 2 lost. Winner - Player 1 ++++++')
            break
    
        turn+=1
        
    menuPoint=input('\nType something for continue. Type 0 for Exit.\n')
SystemExit