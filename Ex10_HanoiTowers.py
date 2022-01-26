# ДЗ: Ханойские башни
# Есть три колышка.  Есть диски разного диаметра. 
# Изначально N дисков упорядоченно надеты на первый колышек таким образом, 
# что диск с наибольшим диаметром находится внизу, а с самым малом наверху. 
# Цель - переместить с первого колышка все диски на третий колышек, сохранив на нём ту же (изначальную) упорядоченность. 
# Для этого используется второй колышек. 
# При перекладывании дисков между колышками есть важное правило: 
# нельзя класть диск большего диаметра на диск с меньшим диаметром.
# Саму механику игры программировать не надо - достаточно запрограммировать саму формулу подсчёта количества шагов.
# Надо написать функцию solve_hanoi_tower, которая принимает количество дисков и 
# возвращает минимальное кол-во ходов за которое можно решить задачу.
# Примеры вызовов и возвратов:
# solve_hanoi_tower(3) >>> 7
# solve_hanoi_tower(5) >>> 31
# solve_hanoi_tower(0) >>> 0
# Передаются только положительные целые >= 0.

print('********* Start of programm *********')

def solve_hanoi_tower(discs):
    return sum([2**(x) for x in range(0, discs)])

menuPoint=1
while menuPoint!='0':

    disk_count=int(input('Enter count of disks:\n'))
    print(solve_hanoi_tower(disk_count))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit