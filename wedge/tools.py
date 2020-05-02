
def time_str(time1: str, time2: str):
    time1_str = '{}{}'.format(time1[:2], time1[3:])
    time2_str = '{}{}'.format(time2[:2], time2[3:])
    time1_int = str_to_num(time1_str)
    time2_int = str_to_num(time2_str)
    if time1_int > time2_int:
        return 1
    elif time1_int == time2_int:
        return 0
    else:
        return -1
    
def date_format2(date: str):
    format_date = '{}-{}'.format(date[5:7], date[8:10])
    return format_date

def str_to_num(str_num: str):
    num = 0
    for e in str_num:
        num *= 10
        num += int(e)
    return num

def date_format1(month: int, day: int):
    if month < 10:
        month_str = '0{}'.format(month)
    else:
        month_str = '{}'.format(month)
    
    if day < 10:
        day_str = '0{}'.format(day)
    else:
        day_str = '{}'.format(day)
    
    path = 'data/2019CoV/2020{}{}_virus.csv'.format(month_str, day_str)
    return path