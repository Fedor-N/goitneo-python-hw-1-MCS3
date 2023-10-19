from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {"name": "Bill", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan", "birthday": datetime(1976, 2, 24)},
    {"name": "Jill", "birthday": datetime(1974, 10, 21)},
    {"name": "Kim", "birthday": datetime(1980, 10, 22)},
    {"name": "Fil ", "birthday": datetime(1980, 10, 23)},
    {"name": "Jim ", "birthday": datetime(1980, 10, 24)},
    {"name": "Kite ", "birthday": datetime(1980, 10, 25)},
    {"name": "Jon ", "birthday": datetime(1980, 10, 26)},
    {"name": "Patrik ", "birthday": datetime(1980, 10, 27)},
    {"name": "Lusi ", "birthday": datetime(1980, 10, 28)},
    {"name": "Ken ", "birthday": datetime(1980, 10, 29)}
]


def get_birthdays_per_week(users):
    birthday_dict = defaultdict(list)
    today = datetime.today().date()
    start = today - timedelta(days=today.weekday())
    end = start + timedelta(days=6)
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        delta_days = (birthday_this_year - end).days
        # print("birthday_this_year - " + str(birthday_this_year))
        # print("delta_days - " + str(delta_days))
        # print("end - " + str(end))
        if delta_days <= 5 and delta_days > -2:
            day_of_week = (birthday_this_year).strftime('%A')
            if day_of_week == "Saturday" or day_of_week == "Sunday":
                day_of_week = "Monday"
            birthday_dict[day_of_week].append(name)

    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")


get_birthdays_per_week(users)
