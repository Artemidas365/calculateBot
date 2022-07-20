def calculator(x, y):
    w = y.replace('-', '.')
    yr0 = int(w[:4])
    mon0 = int(w[5:7])
    day0 = int(w[8:10])
    day1 = int(x[:2])
    mon1 = int(x[3:5])
    yr1 = int(x[6:10])
    yrs = yr0 - yr1

    def month(a, b, c):
        if a > b:
            monss = a - b
            return monss, c
        else:
            monss = a + 12 - b
            c -= 1
            return monss, c

    def day(a, b, c):
        if a > b:
            dayss = a - b
            return dayss, c
        else:
            dayss = a + 30 - b
            c -= 1
            return dayss, c

    mons, yrs = month(mon0, mon1, yrs)
    days, mons = day(day0, day1, mons)
    return days, mons, yrs


def in_days(a,b,c):
    return a + b*30 + c*365


def in_seconds(a):
    return a*86400


def in_hours(a):
    return a*24


def in_weeks(a):
    return a//7
