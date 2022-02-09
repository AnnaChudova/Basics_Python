duration = int(input('Введите продолжительность времени в секундах: '))
day = duration // 86400
hour = duration % 86400 // 3600
minute = duration // 60 % 60
seconds = duration % 60

if duration < 60:
    print(duration, 'сек')
elif duration >= 60 and duration < 3600:
    print(minute, 'мин', seconds, 'сек')
elif duration >= 3600 and duration < 86400:
    print(hour, 'ч', minute, 'мин', seconds, 'сек')
elif duration > 86400:
    print(day, 'дн', hour, 'ч', minute, 'мин', seconds, 'сек')
