import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Повертає відсортований список з `quantity` унікальних випадкових чисел
    у діапазоні від min до max (включно).

    Якщо параметри не відповідають обмеженням:
    - min < 1
    - max > 1000
    - min >= max
    - quantity < 1 або quantity > (max - min + 1)
    — повертається порожній список.
    """
    # Перевірка діапазону
    if min < 1 or max > 1000 or min >= max:
        return []

    # Неможливо вибрати стільки унікальних чисел з цього діапазону
    if quantity < 1 or quantity > (max - min + 1):
        return []

    # Генеруємо унікальні випадкові числа
    numbers = random.sample(range(min, max + 1), quantity)

    # Сортуємо
    numbers.sort()

    return numbers


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)