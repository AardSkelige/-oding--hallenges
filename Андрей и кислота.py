n = int(input())
# print("Введите через пробел количество литров кислоты в каждом резервуаре")
array = list(map(int, input().split()))

# solve
max_value = array[0]
min_value = array[0]
answer = 0

for value in array:
    max_value = max(value, max_value)
    min_value = min(value, min_value)
    if value < max_value:
        answer = -1
        break

if answer == 0:
    print(max_value - min_value)
else:
    print(answer)
