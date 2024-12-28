# datetime module has many fucntions
from datetime import datetime, date, time

# Current date and time
now = datetime.now()
print("Current date and time:", now)

# Current date
today = datetime.today()
print("Today's date:", today)

# Create a specific date
specific_date = date(2023, 12, 28)
print("Specific date:", specific_date)

# Create a specific time
specific_time = time(14, 30, 45)
print("Specific time:", specific_time)

# Create a specific datetime
specific_datetime = datetime(2023, 12, 28, 14, 30, 45)
print("Specific datetime:", specific_datetime)

# some more functions under now
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Format datetime
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted_datetime)

# parsed datetime
parsed_datetime = datetime.strptime(formatted_datetime, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_datetime)


