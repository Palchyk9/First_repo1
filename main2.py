#Перше завдання

from datetime import datetime

def get_days_from_today(date):
    target_date = datetime.strptime(date_string, '%Y-%m-%d').date()

    date_today = datetime.today().date()

    delta = date_today - target_date

    return delta.days


date_string = "2020-10-09"
diferent = get_days_from_today(date_string)
print(diferent)

    


