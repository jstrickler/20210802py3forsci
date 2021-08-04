from datetime import date, datetime, timedelta

today = date.today()
jays_bd = date(2014, 8, 1)

diff = today - jays_bd

years = diff.days // 365
days = diff.days % 365
print(f"Jay is {years} years and {days} days old")
