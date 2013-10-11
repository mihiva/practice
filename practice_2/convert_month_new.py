#-*- encoding: utf-8 -*-
m = input("Enter the month: ")
m = m.capitalize()
dict = {"January" : "1", "February" : "2", "March" : "3", "April" : "4", "May":"5", "June" : "6", "July" : "7", "August" : "8", "September" : "9", "October" : "10", "November" : "11", "December" : "12"}
if (dict.has_key(m)):
  print dict[m]
else:
  print("It is not the month. Try again")