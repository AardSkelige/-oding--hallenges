# Функция ввода и обработки данных
def input_data():
    # Вводим количество рядов в самолете
    number_of_rows_in_plane = int(input())
    # Создаем пустой список мест в самолете
    rows_in_plane = []
    # Считываем содержимое каждого ряда
    for i in range(number_of_rows_in_plane):
        # Убираем лишние пробелы
        row = input().strip()
        # Соединяем все ряды в единый список (список рядов в самолете с учетом занятых мест)
        rows_in_plane.append(row)
    # Вводим количество групп пассажиров
    num_groups = int(input())
    # Создаем переменную для хранения групп пассажиров и их пожеланий
    group_preferences = {}
    # Перебираем диапазон всех групп из указанного количества
    for i in range(num_groups):
        # Разбиваем строку на отдельные элементы (количество, сторона, пожелания)
        group_info = input().split()

        group_quantity = int(group_info[0])
        group_side = group_info[1]
        group_seat_preference = group_info[2]
        group_preferences[i+1] = {'group_quantity': group_quantity,
                                  'side': group_side,
                                  'seat_preference': group_seat_preference}

    return number_of_rows_in_plane, rows_in_plane, num_groups, group_preferences


number_of_rows_in_plane, rows_in_plane, num_groups, group_preferences = input_data()
letters = ['A', 'B', 'C', '_', 'D', 'E', 'F']
for i in range(len(group_preferences)):
    can_seat = False
    group = group_preferences[i+1]
    for i in range(len(rows_in_plane)):
        if group['side'] == 'left':
            if group['group_quantity'] == 1:
                if group['seat_preference'] == 'window':
                    if rows_in_plane[i][0] == '.':
                        rows_in_plane[i] = rows_in_plane[i][:0] + \
                            'X' + rows_in_plane[i][1:]
                        print(
                            f'Passengers can take seats: {i+1}{letters[0]}\n' + "\n".join(rows_in_plane))
                        can_seat = True
                        break
                elif group['seat_preference'] == 'aisle':
                    if rows_in_plane[i][2] == '.':
                        rows_in_plane[i] = rows_in_plane[i][:2] + \
                            'X' + rows_in_plane[i][3:]
                        print(
                            f'Passengers can take seats: {i+1}{letters[2]}\n' + "\n".join(rows_in_plane))
                        can_seat = True
                        break
            elif group['group_quantity'] == 2:
                if group['seat_preference'] == 'window':
                    if rows_in_plane[i][:2] == '..':
                        rows_in_plane[i] = rows_in_plane[i][:0] + \
                            'XX' + rows_in_plane[i][2:]
                        print(
                            f'Passengers can take seats: {i+1}{letters[0]} {i+1}{letters[1]}\n' + "\n".join(rows_in_plane))
                        can_seat = True
                        break
                elif group['seat_preference'] == 'aisle':
                    if rows_in_plane[i][1:3] == '..':
                        rows_in_plane[i] = rows_in_plane[i][:1] + \
                            'XX' + rows_in_plane[i][3:]
                        print(
                            f'Passengers can take seats: {i+1}{letters[1]} {i+1}{letters[2]}\n' + "\n".join(rows_in_plane))
                        can_seat = True
                        break
            elif group['group_quantity'] == 3:
                if rows_in_plane[i][:3] == '...':
                    rows_in_plane[i] = 'XXX' + rows_in_plane[i][3:]
                    print(
                        f'Passengers can take seats: {i+1}{letters[0]} {i+1}{letters[1]} {i+1}{letters[2]}\n' + "\n".join(rows_in_plane))
                    can_seat = True
                    break

        if group['side'] == 'right':
            if group['group_quantity'] == 1:
                if group['seat_preference'] == 'window':
                    if rows_in_plane[i][6] == '.':
                        rows_in_plane[i] = rows_in_plane[i][:6] + 'X'
                        print(
                            f'Passengers can take seats: {i+1}{letters[-1]}\n' + "\n".join(rows_in_plane))
                        can_seat = True
                        break
                elif group['seat_preference'] == 'aisle':
                    if rows_in_plane[i][4] == '.':
                        rows_in_plane[i] = rows_in_plane[i][:4] + \
                            'X' + rows_in_plane[i][5:]
                        print(
                            f'Passengers can take seats: {i+1}{letters[-3]}\n' + "\n".join(rows_in_plane))
                        can_seat = True
                        break
            elif group['group_quantity'] == 2:
                if group['seat_preference'] == 'window':
                    if rows_in_plane[i][5:] == '..':
                        rows_in_plane[i] = rows_in_plane[i][:5] + 'XX'
                        print(
                            f'Passengers can take seats: {i+1}{letters[-2]} {i+1}{letters[-1]}\n' + "\n".join(rows_in_plane))
                        can_seat = True
                        break
                elif group['seat_preference'] == 'aisle':
                    if rows_in_plane[i][4:6] == '..':
                        rows_in_plane[i] = rows_in_plane[i][:4] + \
                            'XX' + rows_in_plane[i][6:]
                        print(
                            f'Passengers can take seats: {i+1}{letters[-3]} {i+1}{letters[-2]}\n' + "\n".join(rows_in_plane))
                        can_seat = True
                        break
            elif group['group_quantity'] == 3:
                if rows_in_plane[i][4:] == '...':
                    rows_in_plane[i] = rows_in_plane[i][:4] + 'XXX'
                    print(
                        f'Passengers can take seats: {i+1}{letters[-3]} {i+1}{letters[-2]} {i+1}{letters[-1]}\n' + "\n".join(rows_in_plane))
                    can_seat = True
                    break
    if can_seat == False:
        print('Cannot fulfill passengers requirements')
