from datetime import datetime

class GetDay():

    def __init__(self, datetime_class=None):
        if datetime_class:
            self.day = datetime_class
        else:
            self.day = datetime.now()

    def get_weekday(self) -> str:
        day_number = self.day.weekday()
        day_and_number = {
            "Monday"    :   0,
            "Tuesday"   :   1,
            "Wednesday" :   2,
            "Thursday"  :   3,
            "Friday"    :   4,
            "Saturday"  :   5,
            "Sunday"    :   6
        }
        for day, number in day_and_number.items():
            if day_number == number:
                return day

    @classmethod
    def get_weekday_from_number(cls, day_number: int) -> str:
        day_and_number = {
            "Monday"    :   0,
            "Tuesday"   :   1,
            "Wednesday" :   2,
            "Thursday"  :   3,
            "Friday"    :   4,
            "Saturday"  :   5,
            "Sunday"    :   6
        }
        for day, number in day_and_number.items():
            if day_number == number:
                return day


# Sample usage

# Create the instance
# today = GetDay()
# or
# today = GetDay(datetime(2017, 2, 2))

# print the date you've passed into the class
# print(today.day)

# get the day of the week in text - this will either return today
# or the day of the datetime object you passed in
# print(today.get_weekday())

# or you can get the day of the week based on the number
# like in the following scenario
# >>> import datetime
# >>> datetime.datetime.today()
# datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
# >>> number = datetime.datetime.today().weekday()
# >>> print(GetDay.get_weekday_from_number(number))
# 'Wednesday'
