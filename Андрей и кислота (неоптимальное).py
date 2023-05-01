print("Введите количество резервуаров")
n = int(input())
print("Введите через пробел количество литров кислоты в каждом резервуаре")
a = list(map(int, input().split()))

min_value = float('inf')
min_index = -1
max_value = float('-inf')
max_index = -1

for i, value in enumerate(a):
    if value < min_value:
        min_value = value
        min_index = i
    if value > max_value:
        max_value = value
        max_index = i

print(f"Минимальное значение {min_value} в резервуаре {min_index+1}")
print(f"Максимальное значение {max_value} в резервуаре {max_index+1}")


def is_ascending(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1] or lst[i] <= 0 or lst[i+1] <= 0:
            return False
    return True


if is_ascending(a) == False:
    print(f'Уровнять резервуары невозможно "-1"')
    print(-1)

else:
    print('Уровнять резервуары возможно')
    counter = 0
    if min_value == max_value:
        print(0)
    else:
        for i in range(len(a)-1):
            if a[i] < max_value:
                print(f"В резервуар #{i+1} нужно добавить {max_value-a[i]} л.")
                a[i] += 1
            counter += 1
        print(counter)
