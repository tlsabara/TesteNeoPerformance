from datetime import datetime
import re


def clear_month(val_month) -> int:
    voc = {
        "JAN": 1,
        "FEV": 2,
        "MAR": 3,
        "ABR": 4,
        "MAI": 5,
        "JUN": 6,
        "JUL": 7,
        "AGO": 8,
        "SET": 9,
        "OUT": 10,
        "NOV": 11,
        "DEZ": 12,
    }

    if str(val_month).isnumeric():
        return int(val_month)
    else:
        return voc.get(str(val_month).upper()[0:3], 0)


def clear_year(val_year) -> int:
    try:
        year = int(val_year)
        if year < 100:
            year += 2000
        elif year < 1000:
            year += 1900
    except Exception:
        year = 1900
    return year

def convert_datetime(str_datetime, format=None) -> datetime:
    format_ = "%d/%m/%Y" if not format else format
    val_datetime = None
    try:
        val_datetime = datetime.strptime(str_datetime, format_)
    except Exception:
        if format:
            val_datetime = convert_datetime(str_datetime, "%m/%d/%Y")
    return val_datetime

def brute_parse_date(str_datetime) -> datetime:
    date = convert_datetime(str_datetime)
    try:
        if not date:
            e1, e2, year = str_datetime.split("/")
            year = clear_year(year)

            if int(e1) > 28 and 1 <= int(e2) <= 12:
                date = datetime(year, int(e2), 1)
            elif int(e2) > 28 and 1 <= int(e1) <= 12:
                date = datetime(year, int(e1), 1)
            else:
                return datetime(year, 1, 1)
        return date
    except Exception:
        raise Exception(f"{str_datetime} não pode ser convertido para data")