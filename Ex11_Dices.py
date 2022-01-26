# Играем в кости. Правила следующие:
# 1. Кидаем пару костей.
# 2. Складываем количество выпавших чисел и прибавляем к общему кол-ву очков
# 3. Повторяем пункты 1 и 2 трижды.
# 4. Если выпадает дуплет (на обоих костях одно и то же число), 
# то кол-во очков обнуляется и последующие броски не считаются.
# Напишите функцию  calc_dice_scores принимающую список кортежей и, возвращающую общее кол-во очков.
# Примеры вызовов и ожидаемый результат:
# calc_dice_scores([(1, 2), (3, 4)s (5, 6)]) >>> 21
# calc_dice_scores([(2, 2), (8 6), (6 4)]) >>> 0
# calc_dice_scores([(4, 5), (4, 5), (4, 5)]) >>> 27

print('********* Start of programm *********')

def calc_dice_scores(lst):
    return sum([x+y for x,y in lst]) if not any([x==y for x,y in lst]) else 0

menuPoint=1
while menuPoint!='0':
    dices=[]
    for x in range(0,3):
        dices.append((int(input(f'Throw {x+1}: Enter x for throw:\n')), int(input(f'Throw {x+1}: Enter y for throw:\n'))))
    print(f'Entered dices: {dices}')
    print(calc_dice_scores(dices))

    menuPoint=input('Type something for continue. Type 0 for Exit.\n')
SystemExit