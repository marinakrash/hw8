import datetime

from collections import defaultdict, OrderedDict

def get_birthdays_per_week(users):
    birth_list=[]
    grouped_birthday = defaultdict(list)
    current_date = (datetime.datetime.now()).date()
    weeks_interval = datetime.timedelta(weeks=1)
    future_week = current_date + weeks_interval
    for i in users:
        birthday=(i['birthday'])
        birthday_new=datetime.date(current_date.year, birthday.month, birthday.day)
        date_list = [current_date + datetime.timedelta(days=x) for x in range(7)]
        if birthday_new in date_list:
            birth_list.append([i['name'], birthday_new.strftime('%A')])
    for name, date in birth_list:
        if date == 'Sunday' or date == 'Saturday':
            date='Monday'
        grouped_birthday[date].append(name)
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    result = OrderedDict()
    for day in week:
        if day in grouped_birthday:
            result[day] = grouped_birthday[day]
    print(result)
    return(result)

