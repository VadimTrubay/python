from prettytable import from_db_cursor

import my_select 


query_table = [
    "Виберіть який запит ви хочете виконати?",
    "1 -- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.",
    "2 -- Знайти студента із найвищим середнім балом з певного предмета.",
    "3 -- Знайти середній бал у групах з певного предмета.",
    "4 -- Знайти середній бал на потоці (по всій таблиці оцінок).",
    "5 -- Знайти які курси читає певний викладач.",
    "6 -- Знайти список студентів у певній групі.",
    "7 -- Знайти оцінки студентів у окремій групі з певного предмета.",
    "8 -- Знайти середній бал, який ставить певний викладач зі своїх предметів.",
    "9 -- Знайти список курсів, які відвідує студент.",
    "10 -- Список курсів, які певному студенту читає певний викладач.",
    "11 -- Середній бал, який певний викладач ставить певному студентові.",
    "12 -- Оцінки студентів у певній групі з певного предмета на останньому занятті.",
    "Будь яке інше число -- Вихід"
]
tooltip = '\n'
for s in query_table:
    tooltip = tooltip + s + '\n'

if __name__ == "__main__":
    print(tooltip)
    while True:
        try:
            query = int(input("Виберіть номер запиту: "))
            match query:
                case 1:
                    result = my_select.select_1()
                case 2:
                    result = my_select.select_2()
                case 3:
                    result = my_select.select_3()
                case 4:
                    result = my_select.select_4()
                case 5:
                    result = my_select.select_5()
                case 6:
                    result = my_select.select_6()
                case 7:
                    result = my_select.select_7()
                case 8:
                    result = my_select.select_8()
                case 9:
                    result = my_select.select_9()
                case 10:
                    result = my_select.select_10()
                case 11:
                    result = my_select.select_11()
                case 12:
                    result = my_select.select_12()
                case _:
                    break
                
            print(query_table[query])
            # print(from_db_cursor(result))
            print(result)
            print()
        except:
            print('Input number, please!')

    print('Finish query')
