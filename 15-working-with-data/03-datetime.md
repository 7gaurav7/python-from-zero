# datetime

## Learning Objectives
- Get the current date and time
- Create a specific date or datetime
- Format a date/time as a string, and parse a string into one
- Calculate durations between dates using `timedelta`

## Concept Explanation
The `datetime` module represents dates/times as objects you can compare,
format, and do arithmetic with -- instead of juggling separate day/month/
year numbers.
```python
from datetime import date, datetime
today = date.today()
now = datetime.now()
```
`date` handles just a calendar date; `datetime` handles a date *and* time.

## Syntax
```python
from datetime import date, datetime, timedelta

date.today(); datetime.now()
date(2026, 12, 25); datetime(2026, 12, 25, 9, 30)
some_date.strftime("%Y-%m-%d")             # format -> string
datetime.strptime(text, "%Y-%m-%d")         # string -> datetime
date1 - date2                                # a timedelta
some_date + timedelta(days=7)
```
Common codes: `%Y` `%m` `%d` `%H` `%M` `%S` `%A` (weekday name) `%B` (month name).

## Examples

**Example 1 - Today's date and current time**
```python
from datetime import date, datetime
print(date.today())
print(datetime.now())
```
Sample output (varies by when you run it):
```
2026-09-06
2026-09-06 14:32:01.123456
```

**Example 2 - Formatting a date**
```python
today = date.today()
print(today.strftime("%B %d, %Y"))
print(today.strftime("%A"))
```
Sample output (varies by date):
```
September 06, 2026
Sunday
```

**Example 3 - Parsing a string into a date**
```python
from datetime import datetime
christmas = datetime.strptime("2026-12-25", "%Y-%m-%d")
print(christmas.year, christmas.month, christmas.day)
```
Expected output: `2026 12 25`

**Example 4 - Date arithmetic with `timedelta`**
```python
from datetime import date, timedelta
start = date(2026, 1, 1)
end = date(2026, 3, 1)
print((end - start).days, "days")
```
Expected output: `59 days`

## Common Mistakes
- Confusing `date` (no time) and `datetime` (date + time).
- Mismatched `strftime`/`strptime` format codes -- the format string must
  exactly match the text's shape, or you get `ValueError`.
- Forgetting subtracting two dates gives a `timedelta`, not a number --
  use `.days`.
- Assuming `date.today()` includes a time -- it never does.

## Practice
1. Print today's date as `"DD/MM/YYYY"`.
2. Print the name of today's weekday.
3. Parse `"2026-07-04"` and print just the month.
4. Calculate days remaining until January 1st of next year.

## Challenge
Write `age_in_days(birth_date_text)` taking a `"YYYY-MM-DD"` string and
returning how many days old that makes someone as of today.

## Mini Project
Add a `date_added` field to the `19-projects` To-Do List App, and a menu
option to show only tasks added in the last 7 days.

## Summary
`datetime` (`date`, `datetime`, `timedelta`) represents dates/times as
objects you can format, parse, compare, and calculate with -- far more
reliable than manual string manipulation.

## Next Step
Continue to [`04-pathlib.md`](04-pathlib.md).
