# Python
# дз
duration = int(input('Введите количество секунд'))
a = duration
if a < 60:
    print(a, 'сек')
else:
    min = a // 60
    sec = a % 60
    if min < 60:
        print(min, 'мин', sec, 'сек')
    else:
        hours = min // 60
        min_from_hours = min % 60
        if hours < 24:
            print(hours, 'час', min_from_hours, 'мин', sec, 'сек')
        else:
            days = hours //24
            hours_from_days = hours % 24
            print(days, 'дн', hours_from_days, 'час', min_from_hours, 'мин', sec, 'сек')