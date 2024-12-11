first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
print(list(first_result))

# second_result = (len(first[i]) == len(second[i]) for i in range(0,3)) - первоначальное решение

# далее, доработанное решение с учетом комментария преподавателя
second_result = (len(first[i]) == len(second[i]) for i in range(len(first))) if (len(first) <= len(second)) \
    else (len(first[i]) == len(second[i]) for i in range(len(second)))

print(list(second_result))
