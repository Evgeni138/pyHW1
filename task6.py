# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
day = int(input())
if day == 1:
    print('понедельник')
elif day == 2:
    print('вторник')
elif day == 3:
    print('среда')
elif day == 4:
    print('четверг')
elif day == 5:
    print('пятница')
elif day == 6:
    print('суббота')
elif day == 7:
    print('воскресенье')
if day > 5:
    print('выходной день')
else:
    print('рабочий день')
