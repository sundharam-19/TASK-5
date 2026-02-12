from datetime import datetime
# Sample datetime object (current date & time)
current_dt = datetime.now()
# Lambda functions to extract year, month, and day
extract_year = lambda dt: dt.year
extract_month = lambda dt: dt.month
extract_day = lambda dt: dt.day
# Display results
print("Current Date & Time:", current_dt)
print("Year:", extract_year(current_dt))
print("Month:", extract_month(current_dt))
print("Day:", extract_day(current_dt))
