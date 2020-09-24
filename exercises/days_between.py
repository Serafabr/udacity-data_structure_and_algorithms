### Given your birthday and the current date, calculate your age in days
### Compensate for leap days
### Assume that the birthday and current date are correct dates

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]


def isLeapYear(year):
  if year % 4 != 0:
    return False
  elif year % 100 != 0:
    return True
  elif year % 400 != 0:
    return False
  else:
    return True


def nextDate(y, m, d):
  result_d = d
  result_m = m
  result_y = y
  currentDaysOfMonths = daysOfMonths[:]
  
  if isLeapYear(y):
    currentDaysOfMonths[1] = 29
  
  if (d == currentDaysOfMonths[m - 1]):
    result_d = 1
    if ( m == 12):
      result_m = 1
      result_y = y + 1
    else:
      result_m = m + 1
  else: 
    result_d = d + 1
  
  return (result_y, result_m, result_d)


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
  y = y1
  m = m1
  d = d1
  
  result = 0
  
  while (d != d2 or m != m2 or y != y2):
    y, m, d = nextDate(y, m, d)
    result += 1
  
  return result


### Testing area
print(daysBetweenDates(2012, 6, 29, 2013, 6, 31))
print(daysBetweenDates(2000, 1, 1, 2000, 2, 2))
print(daysBetweenDates(2000, 1, 1, 2000, 4, 2))
print(daysBetweenDates(2000, 1, 1, 2012, 1, 2))
print(daysBetweenDates(1989, 6, 10, 2089, 6, 10))