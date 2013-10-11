#-*-coding: UTF-8 -*-
dict = {'one' : 'igrok', 'two' : 'igroka', 'many' : 'igrokov' }
def humanizer(n, dict):
  if type(n) != int:
    print "This is not a number"
  else:
    if (n % 10)>=1 and (n % 10)<5:
        if (n % 100)>=11 and (n % 100)<=15:
            print str(n) + " " + dict['many']
        elif n % 10 == 1:
            print str(n) + " " + dict['one']
        else:
            print str(n) + " " + dict['two']
    else:
        print str(n) + " " + dict['many']


humanizer(34, dict)
humanizer(10, dict)
humanizer(300, dict)