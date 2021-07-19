from datetime import *


def date_converter(date_string):
    dates = date_string.split("-")
    date_item = [int(item) for item in dates]
    try:
        new_date = date(date_item[0],date_item[1],date_item[2])
        return new_date
    except ValueError:
        return date(9030,12,30)


def period_start_dates(last_period, cycle_averages,start_str, end_str):
    last_period_date = date_converter(last_period)
    end_date = date_converter(end_str)
    start_date = date_converter(start_str)
    if last_period_date>start_date:
        return {"error":"date not in range"}
    if start_date>end_date:
        return {"error":"date not in range"}
    date_list = []
    while last_period_date < end_date :
        cycle_average = timedelta(days=cycle_averages)
        last_period_date = last_period_date + cycle_average
        if start_date <= last_period_date <= end_date:
            date_list.append(last_period_date)
    return date_list