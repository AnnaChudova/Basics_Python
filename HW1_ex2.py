sums1 = 0
sums2 = 0
odd_num = []
i = 0
while i < 1000:
    i += 1
    if i % 2 != 0:
        x = i ** 3
        odd_num.append(x)
print(odd_num)

# Дальше код списан с разбора д/з.
# Я поняла общий смысл дальнейших действий, но пока не поняла как это работает
# Как разберусь скину вам решение этой задачи в телеграм, чтобы вы видели, что я все поняла )

for x in range(len(odd_num)):
    num_sum = 0
    j = odd_num[x]
    while j:
        num_sum += j % 10
        j = j // 10
    if num_sum % 7 == 0:
        sums1 += odd_num[x]
    num_sum = 0
    j = odd_num[x]
    while j:
        num_sum += j % 10
        j = j // 10
    if num_sum % 7 == 0:
        sums2 += odd_num[x]
print(sums1)
print(sums2)