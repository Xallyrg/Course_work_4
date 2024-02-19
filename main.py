"""
Стартуем программу с приветствия и запросов
1) Какие профессии интересуют
2) Ключевые слова (город, требования, обязанности)
3) Минимальная и максимальная зарплата
4) Сколько запросов вывести
"""
print("Добрый день! Давайте подберем вам работу по душе!")
search_query = input("Введите поисковый запрос (какие вакансии вы ищите):  ")
filter_words = input("Введите ключевые слова через запятую (город, требования, обязанности):  ").lower().split(", ")
while True:
    try:
        salary_from = int(input("Введите минимальную желаемую зарплату:  "))
        if salary_from > 0:
            break
        else:
            print("Попробуйте снова, введите положительное число")
            continue
    except ValueError:
        print("Попробуйте снова, введите число")
        continue

while True:
    try:
        salary_to = int(input("Введите максимальную желаемую зарплату:  "))
        if salary_to > salary_from:
            break
        else:
            print(f"Попробуйте снова, введите число большее чем минимальная зарплата {salary_from}")
            continue
    except ValueError:
        print("Попробуйте снова, введите число")
        continue

while True:
    try:
        top_n = int(input("Введите число - топ N вакансий, которые хотите увидеть:  "))
        if top_n > 0:
            break
        else:
            print("Попробуйте снова, введите положительное число")
            continue
    except ValueError:
        print("Попробуйте снова, введите число")
        continue
