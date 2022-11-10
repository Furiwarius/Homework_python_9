# Создайте программу для игры в ""Крестики-нолики"".

from random import choice as fate


def search_matches(pos_list, vin_position):
    # есть ли в списке позиций игрока победная комбинация
    for vin_list in vin_position:
        meter=0
        for i in pos_list:
            if i in vin_list:meter+=1
        if meter==3: return 1
        else: meter=0
    else:
        return -1


def creation_storages():
    # генерация необходимых данных для отрисовки и работы логики игры

    field = [['1', '2', '3'],['4', '5', '6'],['7', '8', '9']] 
    cells = {str(key):None for key in range(1,10)}       
    positions = get_positions(field)
    return field, cells, positions


def victory_check(field, vin_position):
    # проверка на победу
    x_pos = []
    o_pos = []

    for i, line in enumerate(field):
        for n, column in enumerate(line):
            if column=='X':
                x_pos.append([i, n])
            elif column=='O':
                o_pos.append([i, n])

    for n, value in enumerate([x_pos, o_pos], 1):
        if search_matches(value, vin_position)!=-1:
            return n
    else: return -1


def conclusion(field):
    # вывод на экран поля
    for i in field:
        print(' | '.join(i))
        print('----------')


def get_positions(field):
    # получение позиций кнопок
    
    positions = {}
    for i, line in enumerate(field):
        for j, column in enumerate(line):
            positions[column] = [i, j]
    return positions


def determining_first_move(choice):
    # определение первого хода

    move = fate(['Орел', 'Решка'])
    if move==choice:
        return True, move
    else:
        return False, move


def create_vin_position():
    # генерация победных комбинаций

    vin_position = []
    for i in range(3):
        vin_position.append([[i, n] for n in range(3)])
        vin_position.append([[n, i] for n in range(3)])
    else: 
        vin_position.append([[i,i] for i in range(3)])
        vin_position.append([[0,2], [1,1], [2,0]]) # не придумал как это сгенерировать
    
    return vin_position



