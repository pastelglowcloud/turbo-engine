import datetime

def days_in_month(year, month):
    leap = 0
    long_months = [1,3,5,7,8,10,12]
    if year % 400 == 0:
        leap = 1
    elif year % 100 == 0:
        leap = 0
    elif year % 4 == 0:
        leap = 1
    if month == 2:
        return 28 + leap
    if month in long_months:
        return 31
    return 30
    

def is_valid_date(year, month, day):
    if year < datetime.MINYEAR:
        return False
    elif year > datetime.MAXYEAR:
        return False
    elif month < 1 or month > 12:
        return False
    elif day > days_in_month(year, month) or day < 1:
        return False
    else:
        return True

def days_between(year1, month1, day1, year2, month2, day2):
    if is_valid_date(year1, month1, day1) is False:
        return 0
    elif is_valid_date(year2, month2, day2) is False:
        return 0
    else:
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        if date1 > date2:
            return 0
        else:
            difference = date2 - date1
            return difference.days

def age_in_days(year, month, day):
    today = datetime.date.today()
    if is_valid_date(year, month, day) is False:
        return 0
    else:
        return days_between(year, month, day, today.year, today.month, today.day)