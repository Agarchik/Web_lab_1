groupmates = [

{
"name": "Феникс",
"surname": "Смирнов",
"exams": ["МОБД", "История", "Философия"],
"marks": [4, 4, 5]
},

{
"name": "Кочеринская",
"surname": "Марья",
"exams": ["ДМ", "ИЯ", "ООП"],
"marks": [4, 5, 3]
},

{
"name": "Игорь",
"surname": "Шацкий",
"exams": ["История", "Физра", "КТП"],
"marks": [4, 5, 5]
},

{
"name": "Стёпик",
"surname": "Крутиков",
"exams": ["КТП", "ТИ", "ТВиМС"],
"marks": [4, 3, 3]
},

{
"name": "Олег",
"surname": "Бочаров",
"exams": ["Физра", "Информатика", "ИЯ"],
"marks": [3, 5, 3]
}

]
def print_students(students):
    print('Таблица студентов:')
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

print_students(groupmates)

def print_uppermiddle(students, mark):
    print(u"Таблица студентов чей средний балл выше", mark)
    print(u"Имя".ljust(15), u"Фамилия".ljust(10))
    for student in students:
        if float(sum(student["marks"]) / len(student["marks"])) > float(mark):
            print(student["name"].ljust(15), student["surname"].ljust(10))

print_uppermiddle(groupmates, input(u"Введите балл: "))

     