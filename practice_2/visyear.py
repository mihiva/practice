year = input ("Enter the year: ")
if type(year) != int:
  print "This is not a year"
else:
  if year % 400==0:
    print("Leap year")
  elif year % 100 == 0:
    print("Is not leap year")
  elif year % 4 == 0:
    print("Leap year")
  else:
    print("Is not leap year")