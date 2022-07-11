Random python utils I'm making for my own use. Also using this to apply some basic OOP  

```
pip install wise-py-utils
```

```py
>>> from wise.<util_file> import <UtilClass>

# Example:
>>> from wise.datetimeutils import GetDay
```


Enter the specific directory to get more about each utility.

## :spiral_calendar: [datetime-utils](/datetime-utils)

### [get_day](/datetime-utils/get_day.py)

Returns a string containing the weekday of the current or specified date.


## :computer: [cpu-utils](/processor-utils)

## :pencil: [typo-remover](/enter-typos)


# In depth info

# Datetime utils

## [get_day](get_day.py)
The python datetime module is very versatile however as shown in [this](https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date) stackoverflow answer. **Getting a date's weekday as a string is not so simple.** Python's `datetime. datetime.weekday()` returns an integer, 0 for Monday ... ... and 6 for Sunday.  

This module allows me to get a string containing the date (current or otherwise specified) with a single method.

### Examples

Simply get the current day of the week
```py
today = GetDay()
print(today.get_weekday())

Output:
'Saturday'
```

Get the day of a specified date
```py
from datetime import datetime
today = GetDay(datetime(2017, 2, 2))
print(today.get_weekday())

Output:
'Thursday'
```

Get the day based on the weekday number using the `get_weekday_from_number() classmethod
```py
>>> import datetime
>>> number = datetime.datetime.today().weekday()
>>> print(number)
1
>>> print(GetDay.get_weekday_from_number(number))
'Tuesday'
``

# Enter typos

Often when hitting enter, I accidentally hit a key next to it. Often the resulting input can end up looking like this.

```py
characters = ["/", "'" "\" "]"]
input = "<regular input> <random-character><enter>"
```

This library is designed to remove trailing special characters from strings and integers and return what the user actually mean to enter.


# Scan files

Scans a specified file for a regex or string pattern and returns a list of all the results`
