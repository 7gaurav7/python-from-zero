"""15 - Working with Data: datetime
Some outputs vary depending on when you run this."""
from datetime import date, datetime, timedelta

today = date.today()
print(today)
print(datetime.now())

print(today.strftime("%B %d, %Y"))
print(today.strftime("%A"))

christmas = datetime.strptime("2026-12-25", "%Y-%m-%d")
print(christmas.year, christmas.month, christmas.day)

start = date(2026, 1, 1)
end = date(2026, 3, 1)
print((end - start).days, "days")

next_week = today + timedelta(days=7)
print(next_week)
