# Напишите функцию any_duplicates, которая принимает 
# двумерный массив размера 3х3 (9 элементов).
# Двумерный массив заполнен числами от 1 до 9.
# Функция должна вернуть False, если в массиве 
# все числа от 1 до 9 встречаются ровно один раз.
# В противном случае True. 
# Примеры вызовов:
# any_duplicates[[1,2,3],[4,5,6],[7,8,9]] >>> False
# any_duplicates[[1,1,3],[4,5,6],[7,8,9]] >>> True (1 повторяется)

print('********* Start of programm *********')

def any_duplicates(square):
    new_lst=[]
    for x in square:
        for y in x:
            new_lst.append(y)
    if len(set(new_lst))==len(new_lst):
        return False
    else:
        return True

menuPoint=1
while menuPoint!='0':

    arr1=[]
    for x in range(0,3):
        arr1.append([int(input(f'Enter {x+1}:{y+1} for list: \n')) for y in range (0,3)])
    print(any_duplicates(arr1))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit