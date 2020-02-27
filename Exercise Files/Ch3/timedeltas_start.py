#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("today is: "+ str(now))

# print today's date one year from now
print("one year from now it will be: " + str(now+timedelta(days=365)))

# create a timedelta that uses more than one argument
print("In 2 days and 3 weeks it will be: " + str(now + timedelta(days=2,weeks=3)))

# calculate the date 1 week ago, formatted as a string
print("One week ago was:" + str(now - timedelta(weeks=1)))
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was: " + s)
### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)
ny = date(today.year, 1, 1)

# use date comparison to see if April Fool's has already gone for this year
if afd < today:
    print("April fools day already went by %d days ago" % (today - afd).days)
    afd = afd.replace(year=today.year+1)

if ny < today:
    print("New years already went by %d days ago" % (today - ny).days)
    ny = ny.replace(year=today.year+1)
# if it has, use the replace() function to get the date for next year
time_to_afd=afd-today
print("It's just", time_to_afd.days, "days until April Fool's day")
time_to_ny=ny-today
print("New years is in", time_to_ny.days, "Days")
# Now calculate the amount of time until April Fool's Day  


