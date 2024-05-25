class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Приватний метод для хешування ключа"""
        return hash(key) % self.size

    def insert(self, key, value):
        """Метод для вставки ключ-значення в хеш-таблицю"""
        index = self._hash(key)
        # Перевіряємо, чи існує вже такий ключ
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        # Якщо ключ не знайдено, додаємо нову пару
        self.table[index].append([key, value])

    def search(self, key):
        """Метод для пошуку значення за ключем у хеш-таблиці"""
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None

    def delete(self, key):
        """Метод для видалення пари ключ-значення з хеш-таблиці"""
        index = self._hash(key)
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]
                return True
        return False

# Приклад використання
ht = HashTable()

# Вставка ключ-значення
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("cherry", 30)

# Пошук значення за ключем
print("Значення для 'apple':", ht.search("apple"))  # Виведе 10

# Видалення ключ-значення
ht.delete("banana")

# Спроба пошуку видаленого значення
print("Значення для 'banana':", ht.search("banana"))  # Виведе None