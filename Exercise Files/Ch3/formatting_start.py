#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()

  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  # print(now.strftime("The current year is %Y"))
  # print(now.strftime("%a, %d %B, %y"))
  # # Wed, 26 February, 20

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("Locale date and time: %c"))
  print(now.strftime("Locale date: %x"))
  print(now.strftime("Locale time: %X"))
  # Locale date and time: Wed Feb 26 12: 31:50 2020
  # Locale date: 02 / 26 / 20
  # Locale time: 12:31: 50

  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime("Current time: %I:%M:%S %p"))
  print(now.strftime("Current time: %H:%M"))

if __name__ == "__main__":
  main();
