rept = {"python": "питон", "anaconda": "анаконда", "tortoize": "черепаха"}

# Добавление пары "snake" - "змея"
rept["snake"] = "змея"

# Исправление ключа "tortoize" на "tortoise"
rept["tortoise"] = rept.pop("tortoize")

# Вывод сообщений для каждого слова в словаре
for key, value in rept.items():
    print(f"{value.capitalize()} по-английски будет {key}.")

2

cnt = ["Andorra", "Belarus", "Denmark", "Kenya", "Jamaica", "Romania"]
fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]

country_index_dict = dict(zip(cnt, fh))

3

pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]

calc = {}

for pair in pairs:
    product = pair[0] * pair[1]
    calc[pair] = product

print(calc)

4

grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5,
          'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
          'Ursula': 4, 'Viktor': 5}

excel = []
good = []
satisf = []
bad = []

for student, grade in grades.items():
    print(f"{student}: {grade}")
    if grade == 5:
        excel.append(student)
    elif grade == 4:
        good.append(student)
    elif grade == 3:
        satisf.append(student)
    else:
        bad.append(student)

print("Очень хорошие оценки (Excel):")
for student in excel:
    print(student)

print("Хорошие оценки (Good):")
for student in good:
    print(student)

print("Удовлетворительные оценки (Satisf):")
for student in satisf:
    print(student)

print("Плохие оценки (Bad):")
for student in bad:
    print(student)