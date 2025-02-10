import datetime

# 1
def five_days_ago():
	return datetime.datetime.now() + datetime.timedelta(-5)

# 2
def three_days():
	date = datetime.datetime.now() + datetime.timedelta(-1)
	for i in range(3):
		print(date)
		date += datetime.timedelta(1)

# 3
def drop_microseconds(datetime):
	return datetime.replace(microsecond=0)

# 4
def date_difference(date1, date2):
	return (date2 - date1).total_seconds()