def create_user_lst(n: int):
    lst = []
    a = int(input("Введите число: "))
    for i in range(n):
        a = int(input("Введите число: "))
        lst.append(a)
    return lst


def print_and_sum_elements(numbers: list):
    suma = 0
    for element in numbers:
        print(element)
        suma += element
    return suma


def process_strings(strings: list):
    result = []  # создаю переменную в которую сложу список с элементами из списка strings
    for element in strings:  # перебераю элементы из списка strings
        result.append(
            element.upper()
        )  # добовляю в список result все значения из переменной element и с помощью метода upper делаю их в верхний регистр
    return result


def slice_and_reverse(lst: list):
    sp1 = ["first_3", "last_2", "middle_3_7", "reversed_list"]
    dic = {}
    dic[sp1[0]] = lst[0:3]
    dic[sp1[1]] = lst[-2:]
    dic[sp1[2]] = lst[2:7]
    dic[sp1[3]] = lst[::-1]
    return dic


def filter_positive(numbers: list):
    lst = []
    for i in numbers:
        print(i)
        if i >= 0:
            lst.append(i)
    return lst


def count_vowels(text: str):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in text:
        if ch in vowels:
            count += 1
            print(f"гласных {ch}")
    return count


def total_fruit_price(fruits: dict):
    suma = 0
    for fruit in fruits:
        valuta = fruits[fruit]
        suma += valuta
        # print(valuta)
        # print(fruit)
    print(fruits)
    return suma


def average_marks(students: dict):
    dic = {}
    for bal in students:
        total = sum(students[bal])
        srednee = total / len(students[bal])
        dic[bal] = srednee
    return dic


def sum_of_evens(numbers: list):
    suma = 0
    for num in numbers:
        if num % 2 == 0:
            suma += num
    return suma


def multiply_list(numbers: list):
    mult = 1
    for num in numbers:
        mult *= num
    return mult


def reverse_strings(strings):
    return [s[::-1] for s in strings]


if __name__ == "__main__":
    n = int(input("Введите число, чтобы завершить ввод: "))
    spisok = create_user_lst(n)
    print(spisok)

    numbers = [10, 3, 5, 12, 7]
    numb = print_and_sum_elements(numbers)
    print(numb)

    strings = ["milk", "apple", "car"]
    print(sum(len(s) for s in strings))
    up = process_strings(strings)  # тут я добовляю в up список result
    for (
        word
    ) in up:  # из переменной up в которой лежит список по очереди достаю каждый элемент
        print(word)

    lst = [1, 2, 3, 4, 5, 6, 7, 9, 10]
    slovar = slice_and_reverse(lst)
    print(slovar)

    text = input("введите текст")
    glasnie = count_vowels(text)
    print(glasnie)

    fruits = {"apple": 100, "banana": 80, "orange": 120}
    frukt = total_fruit_price(fruits)
    print(frukt)

    students = {"Вася": [5, 4, 3], "Петя": [4, 4, 5], "Маша": [5, 5, 5]}
    ocenka = average_marks(students)
    print(ocenka)

    numbers = [1, 2, 3, 4, 10, 11]
    chet = sum_of_evens(numbers)
    print(chet)

    numbers = [2, 3, 4]
    umnozenie = multiply_list(numbers)
    print(umnozenie)

    strings = ["abc", "hello", "python"]
    perevert = reverse_strings(strings)
    print(perevert)
