from datetime import date, datetime, timedelta


def __get_current_week():
    now = datetime.now()
    current_weekday = now.weekday()
    if current_weekday < 5:
        week_start = now - timedelta(days=0 + current_weekday)
    else:
        week_start = now - timedelta(days=current_weekday - 4)
    return [week_start.date(), week_start.date() + timedelta(days=7)]


def get_birthdays_per_week(data):
    WEEKDAYS = ["", "monday", "tuesday", "wednesday", "thursday", "friday"]
    congratulate = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": []}
    if data:
        for contact in data:
            if contact["birthday"]:
                birth_day = contact["birthday"]
                current_date = datetime.now()
                new_birthday = birth_day.replace(year=current_date.year)
                birthday_weekday = new_birthday.weekday()
                if __get_current_week()[0] <= new_birthday < __get_current_week()[1]:
                    if birthday_weekday < 5:
                        congratulate[WEEKDAYS[birthday_weekday]].append(contact["name"])
                    else:
                        congratulate["monday"].append(contact["name"])
            if not congratulate.values():
                return {}
            else:
                return congratulate
    else:
        return {}

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1986, 11, 5).date()},
        {"name": "Vad Tr", "birthday": datetime(1979, 11, 7).date()},
        {"name": "J NNIkr edf", "birthday": datetime(1999, 11, 10).date()},
        {"name": "ert fv", "birthday": datetime(1956, 11, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    # for day_name, names in result.items():
    #     print(f"{day_name}: {', '.join(names)}")