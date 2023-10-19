

"""
year %4==0&
year%106!=0/year%400==0
year%400==0

"""
def isleapYear(year):
  if(year%4==0 and year%100!=0)or year%400==0:
    return True
  else:
    return False

year=int(input("enter a year:"))

if isleapYear(year):
  print('{} is a leapYear.'.format(year))
else:
  print('{} is not a leapYear.'.format(year))