
def _leap_year(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def check_date(date: str) -> bool:
    day, month, year = list(map(int, date.split('.')))
    print(day, month, year)
    if month == 2 and _leap_year(year) == False:
        if day > 28:
            return False
    if month == 2 and _leap_year(year):
        if day > 29:
            return False
    if month in [4, 6, 9, 11]:
        if day > 30:
            return False
    if day > 31:
        return False
    else:
        return True
