from datetime import datetime, date

def get_days_from_today(date_text: str) -> int:
    """
    Приймає дату у форматі 'YYYY-MM-DD' і повертає
    кількість днів від цієї дати до сьогоднішньої.
    Якщо дата в майбутньому – результат буде від’ємним.
    Якщо формат неправильний – повертає None.
    """
    try:
        user_date = datetime.strptime(date_text, "%Y-%m-%d").date()
    except ValueError:
        # Обробка неправильного формату дати
        print("Помилка: дата має бути у форматі 'YYYY-MM-DD', наприклад '2020-10-09'")
        return None

    today = date.today()
    days_passed = (today - user_date).days
    return days_passed


if __name__ == "__main__":
    # Тестовий запуск – для себе, автотести це не чіпають
    example = "2021-10-09"
    result = get_days_from_today(example)
    print(f"Від дати {example} до сьогодні: {result} днів")