from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    today = date.today()
    upcoming = []

    for user in users:
        # 1. Парсимо день народження з рядка
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # 2. Переносимо ДН на поточний рік
        birthday_this_year = birthday.replace(year=today.year)

        # 3. Якщо в цьому році ДН уже минув, дивимось наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # 4. Різниця в днях між сьогодні і ДН
        days_diff = (birthday_this_year - today).days

        # 5. Якщо ДН протягом наступних 7 днів (включно з сьогодні)
        if 0 <= days_diff <= 7:
            congratulation_date = birthday_this_year

            # 6. Якщо це субота або неділя – переносимо на понеділок
            if congratulation_date.weekday() == 5:      # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:    # неділя
                congratulation_date += timedelta(days=1)

            # 7. Додаємо у підсумковий список
            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1988.11.15"},
        {"name": "Michael Brown", "birthday": "1992.11.16"},
        {"name": "Charlotte White", "birthday": "1992.11.20"},
        {"name": "Benjamin Harris", "birthday": "1985.11.21"},
    ]
    print(get_upcoming_birthdays(users))