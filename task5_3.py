#Алгоритм Боєра-Мура

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0:
        return 0
    
    last = {}
    for i in range(m):
        last[pattern[i]] = i

    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    
    return -1

#Алгоритм Кнута-Морріса-Пратта

def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)
    
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1

#Алгоритм Рабіна-Карпа

def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    
    if m == 0:
        return 0
    
    for i in range(m - 1):
        h = (h * d) % q
    
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    
    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i
        
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    
    return -1

#Вимірювання часу виконання

import timeit

# Завантаження тексту з файлу
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Функція для вимірювання часу виконання алгоритму
def measure_time(func, text, pattern):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}('{text}', '{pattern}')"
    times = timeit.repeat(stmt, setup=setup_code, repeat=5, number=1)
    return min(times)

# Основна функція для порівняння алгоритмів
def compare_algorithms(text1, text2, pattern_existing, pattern_non_existing):
    algorithms = [boyer_moore, kmp_search, rabin_karp]

    print("Тестування для статті 1:")
    for algorithm in algorithms:
        time_existing = measure_time(algorithm, text1, pattern_existing)
        time_non_existing = measure_time(algorithm, text1, pattern_non_existing)
        print(f"{algorithm.__name__} - Існуючий підрядок: {time_existing:.6f}s, Неіснуючий підрядок: {time_non_existing:.6f}s")

    print("\nТестування для статті 2:")
    for algorithm in algorithms:
        time_existing = measure_time(algorithm, text2, pattern_existing)
        time_non_existing = measure_time(algorithm, text2, pattern_non_existing)
        print(f"{algorithm.__name__} - Існуючий підрядок: {time_existing:.6fs}, Неіснуючий підрядок: {time_non_existing:.6fs}")

# Завантаження текстів
text1 = load_text("article1.txt")
text2 = load_text("article2.txt")

# Визначення підрядків для тестування
pattern_existing = "За всю історію комп'ютерних наук склалося розуміння, які алгоритми та структури даних (способи їх зберігання) потрібні для вирішення практичних завдань, певний набір, який повинен знати кожен розробник. Наприклад, сортування: товари в магазині сортують за вартістю або терміну придатності, а ресторани – за віддаленістю або рейтингу. Хеш-таблиці допомагають перевірити коректність пароля та не зберігати його на сайті у відкритому вигляді, графи – знаходити найкоротший шлях і зберігати зв'язки між користувачами в соцмережах."
pattern_non_existing = "Подальші два роки запам’яталися встановленням нових рекордів, адже́ кількість учасників збільшилася вдвічі. До речі, дюк де Рішельє також долучається до цієї події. Четвертий рік поспіль святковий гардероб герцога поповнюється найрізноманітнішими виши́ванками: блакитно-синій і яскраво-червоний, жовтогарячий і ніжно-зелений – ось палітра його ви́шитих візерунків."

# Порівняння алгоритмів
compare_algorithms(text1, text2, pattern_existing, pattern_non_existing)
