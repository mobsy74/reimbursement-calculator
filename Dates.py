import datetime

start_date_input = '9/1/15'
end_date_input = '9/3/2015'
in_date_str = '9/2/15'
out_date_str = '9/4/15'
ONE_DAY = datetime.timedelta(days=1)


class DatetimeRange:
    def __init__(self, dt1, dt2):
        self._dt1 = dt1
        self._dt2 = dt2

    def __contains__(self, dt):
        return self._dt1 < dt < self._dt2


# startDate = datetime.date.strftime(startDateStr,%m/%d/%y)
# startDate = datetime.datetime.strptime(startDateStr, '%m/%d/%y').date()
# print(startDate)
# endDate = startDate + oneDay
# print(endDate)
#
# testDate = datetime.datetime.strptime(testDateStr, '%m/%d/%y').date()
# print(testDate)


def get_date(date_str):
    try:
        converted_date = datetime.datetime.strptime(date_str, '%m/%d/%y').date()
        print(converted_date)
    except:
        try:
            converted_date = datetime.datetime.strptime(date_str, '%m/%d/%Y').date()
            print(converted_date)
        except:
            print('Oops!  Please enter dates in the format mm/dd/yy or mm/dd/yyyy.')
    return converted_date


start = get_date(start_date_input)
end = get_date(end_date_input)

workingDateRange = DatetimeRange(start, end)

if workingDateRange.__contains__(get_date(in_date_str)):
    print("it's in!")
else:
    print("nope")

if workingDateRange.__contains__(get_date(out_date_str)):
    print("it's in!")
else:
    print("nope")