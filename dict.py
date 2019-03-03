timetable = {
    'SU 1162': 'Ростов-на-Дону',
    'SU 2124': 'Солоники',
    'SU 2380': 'Женева'

}

print(timetable)
print(timetable['SU 2124']) # Доступ на чтение
timetable['SU 2124'] = 'Пакистан'
print(timetable)



timetable['SU 2596'] = 'Венеция'
print(timetable)


print('SU 2596' in timetable) # проверяет на ключи

for key in timetable:
    print(key, end=' ')
    print(timetable[key])


for key, value in timetable.items():
    print(key, value)
