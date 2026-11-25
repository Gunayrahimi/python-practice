"""
30 Python Programming Exercises
Organized into 3 levels:
1. Beginner (1-10)
2. Intermediate (11-20)
3. Advanced (21-30)

Each exercise is a separate function or class.
Run this file with: python python_practice_30.py

The examples at the bottom run automatically.
"""

from collections import Counter, deque
import json
import re
from pathlib import Path as FilePath


# ============================================================
# BEGINNER EXERCISES (1-10)
# ============================================================

# 1. Check whether a number is prime.
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


# 2. Calculate the factorial of a non-negative integer.
def factorial(number):
    if number < 0:
        raise ValueError("Number must be non-negative.")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


# 3. Find the largest digit in a non-negative integer.
def largest_digit(number):
    if number < 0:
        raise ValueError("Number must be non-negative.")
    return max(int(digit) for digit in str(number))


# 4. Reverse the digits of an integer.
def reverse_number(number):
    sign = -1 if number < 0 else 1
    return sign * int(str(abs(number))[::-1])


# 5. Check whether an integer is a palindrome.
def is_number_palindrome(number):
    return number >= 0 and str(number) == str(number)[::-1]


# 6. Calculate the greatest common divisor and least common multiple.
def gcd_lcm(a, b):
    x, y = abs(a), abs(b)
    while y:
        x, y = y, x % y
    gcd_value = x
    lcm_value = 0 if a == 0 or b == 0 else abs(a * b) // gcd_value
    return gcd_value, lcm_value


# 7. Create a centered star pyramid.
def star_pyramid(rows):
    if rows < 1:
        raise ValueError("Rows must be at least 1.")
    return "\n".join(
        " " * (rows - row) + "*" * (2 * row - 1)
        for row in range(1, rows + 1)
    )


# 8. Count vowels and consonants in a string.
def count_vowels_consonants(text):
    vowels = set("aeiou")
    vowel_count = 0
    consonant_count = 0
    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count


# 9. Remove duplicates from a list while preserving order.
def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


# 10. Find the second-largest distinct number in a list.
def second_largest(numbers):
    unique_numbers = sorted(set(numbers), reverse=True)
    if len(unique_numbers) < 2:
        raise ValueError("At least two distinct numbers are required.")
    return unique_numbers[1]


# ============================================================
# INTERMEDIATE EXERCISES (11-20)
# ============================================================

# 11. Sort a list using bubble sort.
def bubble_sort(numbers):
    result = numbers[:]
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result


# 12. Find common elements in two lists without duplicates.
def common_elements(first, second):
    second_set = set(second)
    result = []
    for item in first:
        if item in second_set and item not in result:
            result.append(item)
    return result


# 13. Check whether two strings are anagrams (ignoring spaces and case).
def are_anagrams(first, second):
    normalize = lambda value: sorted(char.lower() for char in value if char.isalnum())
    return normalize(first) == normalize(second)


# 14. Count the frequency of each word in a sentence.
def word_frequency(sentence):
    words = re.findall(r"\b[\w']+\b", sentence.lower())
    return dict(Counter(words))


# 15. Build a calculator using separate functions.
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


# 16. Manage student grades using a dictionary.
class StudentManager:
    def __init__(self):
        self.grades = {}

    def add_student(self, name, grade):
        if not 0 <= grade <= 20:
            raise ValueError("Grade must be between 0 and 20.")
        self.grades[name] = grade

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def highest_student(self):
        if not self.grades:
            return None
        return max(self.grades, key=self.grades.get)


# 17. Find the most frequent item in a list.
def most_frequent(items):
    if not items:
        raise ValueError("The list cannot be empty.")
    counts = Counter(items)
    return counts.most_common(1)[0]


# 18. Convert a non-negative decimal integer to binary without bin().
def decimal_to_binary(number):
    if number < 0:
        raise ValueError("Number must be non-negative.")
    if number == 0:
        return "0"
    bits = []
    while number > 0:
        bits.append(str(number % 2))
        number //= 2
    return "".join(reversed(bits))


# 19. Check a password against simple rules.
def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("At least 8 characters")
    if not re.search(r"[A-Z]", password):
        errors.append("At least one uppercase letter")
    if not re.search(r"[a-z]", password):
        errors.append("At least one lowercase letter")
    if not re.search(r"\d", password):
        errors.append("At least one digit")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=]", password):
        errors.append("At least one special character")
    return len(errors) == 0, errors


# 20. Create a simple contact manager.
class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add(self, name, phone):
        self.contacts[name] = phone

    def find(self, name):
        return self.contacts.get(name)

    def remove(self, name):
        return self.contacts.pop(name, None)


# ============================================================
# ADVANCED EXERCISES (21-30)
# ============================================================

# 21. Perform binary search on a sorted list.
def binary_search(numbers, target):
    left, right = 0, len(numbers) - 1
    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


# 22. Merge two sorted lists without using sort().
def merge_sorted(first, second):
    result = []
    i = j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1
    result.extend(first[i:])
    result.extend(second[j:])
    return result


# 23. Solve the N-Queens problem and return one board arrangement.
def solve_n_queens(n):
    if n < 1:
        return None

    board = [-1] * n
    used_columns = set()
    used_diagonals_down = set()
    used_diagonals_up = set()

    def place(row):
        if row == n:
            return True
        for column in range(n):
            diagonal_down = row - column
            diagonal_up = row + column
            if (column in used_columns or
                    diagonal_down in used_diagonals_down or
                    diagonal_up in used_diagonals_up):
                continue

            board[row] = column
            used_columns.add(column)
            used_diagonals_down.add(diagonal_down)
            used_diagonals_up.add(diagonal_up)

            if place(row + 1):
                return True

            used_columns.remove(column)
            used_diagonals_down.remove(diagonal_down)
            used_diagonals_up.remove(diagonal_up)
            board[row] = -1
        return False

    if not place(0):
        return None

    return [
        "".join("Q" if column == queen_column else "." for column in range(n))
        for queen_column in board
    ]


# 24. Find shortest distances from a start node using BFS.
def bfs_shortest_paths(graph, start):
    distances = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    return distances


# 25. Build a small library system using classes.
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, copies=1):
        if copies < 0:
            raise ValueError("Copies cannot be negative.")
        self.books[title] = self.books.get(title, 0) + copies

    def borrow(self, title):
        if self.books.get(title, 0) <= 0:
            return False
        self.books[title] -= 1
        return True

    def return_book(self, title):
        self.books[title] = self.books.get(title, 0) + 1


# 26. Demonstrate inheritance with bank accounts.
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate


# 27. Save and load users in a JSON file.
# Educational example only: real applications must hash passwords.
class UserAuth:
    def __init__(self, filename="users_demo.json"):
        self.filename = FilePath(filename)
        self.users = self._load()

    def _load(self):
        if not self.filename.exists():
            return {}
        try:
            with self.filename.open("r", encoding="utf-8") as file:
                data = json.load(file)
            return data if isinstance(data, dict) else {}
        except (json.JSONDecodeError, OSError):
            return {}

    def register(self, username, password):
        if not username or not password or username in self.users:
            return False
        self.users[username] = password
        self._save()
        return True

    def login(self, username, password):
        return self.users.get(username) == password

    def _save(self):
        with self.filename.open("w", encoding="utf-8") as file:
            json.dump(self.users, file, indent=4)


# 28. Create a to-do list that persists in a JSON file.
class TodoList:
    def __init__(self, filename="todos_demo.json"):
        self.filename = FilePath(filename)
        self.tasks = self._load()

    def _load(self):
        if not self.filename.exists():
            return []
        try:
            with self.filename.open("r", encoding="utf-8") as file:
                data = json.load(file)
            return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            return []

    def add(self, task):
        if task.strip():
            self.tasks.append({"task": task, "done": False})
            self._save()

    def complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            self._save()
            return True
        return False

    def _save(self):
        with self.filename.open("w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=4, ensure_ascii=False)


# 29. Manage product stock and calculate inventory value.
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity, price):
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price cannot be negative.")
        if name not in self.products:
            self.products[name] = {"quantity": 0, "price": price}
        self.products[name]["quantity"] += quantity
        self.products[name]["price"] = price

    def sell(self, name, quantity):
        if quantity <= 0 or name not in self.products:
            return False
        if self.products[name]["quantity"] < quantity:
            return False
        self.products[name]["quantity"] -= quantity
        return True

    def total_value(self):
        return sum(
            item["quantity"] * item["price"]
            for item in self.products.values()
        )


# 30. Play a word-guessing game in the terminal.
def word_guessing_game():
    import random

    words = ["python", "computer", "programming", "keyboard", "algorithm"]
    secret = random.choice(words)
    guessed = set()
    attempts = 6

    print("Guess the hidden word. You have 6 wrong attempts.")
    while attempts > 0:
        visible = " ".join(letter if letter in guessed else "_" for letter in secret)
        print("Word:", visible)
        if all(letter in guessed for letter in secret):
            print("You won!")
            return

        guess = input("Enter one letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue
        if guess in guessed:
            print("You already tried that letter.")
            continue

        guessed.add(guess)
        if guess not in secret:
            attempts -= 1
            print("Wrong! Attempts left:", attempts)

    print("Game over. The word was:", secret)


# ============================================================
# SAMPLE TESTS
# ============================================================

if __name__ == "__main__":
    print("BEGINNER")
    print("1. Is 17 prime?", is_prime(17))
    print("2. 5 factorial:", factorial(5))
    print("3. Largest digit in 5831:", largest_digit(5831))
    print("4. Reverse of -123:", reverse_number(-123))
    print("5. Is 1221 a palindrome?", is_number_palindrome(1221))
    print("6. GCD and LCM of 12 and 18:", gcd_lcm(12, 18))
    print("7. Star pyramid:\n" + star_pyramid(4))
    print("8. Vowels and consonants:", count_vowels_consonants("Hello World"))
    print("9. Remove duplicates:", remove_duplicates([1, 2, 2, 3, 1]))
    print("10. Second largest:", second_largest([4, 9, 2, 9, 7]))

    print("\nINTERMEDIATE")
    print("11. Bubble sort:", bubble_sort([5, 1, 4, 2, 8]))
    print("12. Common elements:", common_elements([1, 2, 3], [2, 3, 4]))
    print("13. Are anagrams?", are_anagrams("Listen", "Silent"))
    print("14. Word frequency:", word_frequency("Python is fun and Python is useful"))
    print("15. 10 / 2:", divide(10, 2))

    students = StudentManager()
    students.add_student("Sara", 18)
    students.add_student("Mina", 20)
    print("16. Student average and highest:", students.average(), students.highest_student())

    print("17. Most frequent item:", most_frequent([1, 2, 2, 3, 2, 4]))
    print("18. Decimal 13 in binary:", decimal_to_binary(13))
    print("19. Password validation:", validate_password("Python123!"))
    contacts = ContactManager()
    contacts.add("Sara", "09120000000")
    print("20. Find contact:", contacts.find("Sara"))

    print("\nADVANCED")
    print("21. Binary search for 7:", binary_search([1, 3, 5, 7, 9], 7))
    print("22. Merge sorted lists:", merge_sorted([1, 4, 7], [2, 3, 8]))
    print("23. N-Queens solution for 4:", solve_n_queens(4))
    graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}
    print("24. BFS distances:", bfs_shortest_paths(graph, "A"))

    library = Library()
    library.add_book("Python Basics", 2)
    library.borrow("Python Basics")
    print("25. Library inventory:", library.books)

    account = SavingsAccount("Alex", 1000, 0.05)
    account.add_interest()
    print("26. Savings balance:", account.balance)

    inventory = Inventory()
    inventory.add_product("Laptop", 3, 500)
    inventory.sell("Laptop", 1)
    print("29. Inventory value:", inventory.total_value())

    print("\nAll sample tests finished.")
    print("Exercise 30 is interactive. Run word_guessing_game() to play.")
