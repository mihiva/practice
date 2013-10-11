def zero():
  print """********
*      *
*      *
*      *
*      *
*      *
*      *
********"""

def one():
  print """       *
      **
     * *
    *  *
       *
       *
       *
       *"""

def two():
  print """********
       *
       *
********
*       
*       
********
        """

def three():
  print """*******
       *
       *
********
       *
       *
       *
********"""

def four():
  print """*      *
*      *
*      *
*      *
********
       *
       *
       *"""

def five():
  print """********
*       
*       
********
       *
       *
       *
********"""

def six():
  print """********
*       
*       
********
*      *
*      *
*      *
********"""

def seven():
  print """********
       *
       *
       *
       *
       *
       *
       *"""

def eight():
  print """********
*      *
*      *
********
*      *
*      *
*      *
********"""

def nine():
  print """********
*      *
*      *
*      *
********
       *
       *
********"""

dict = {0 : zero, 1 : one, 2 : two, 3 : three, 4 : four, 5 : five, 6 : six, 7 : seven, 8 : eight, 9 : nine,}
numb = ""
f = 1
while f:
  numb = input("Enter the number('ex' for exit):")
  if numb == "ex":
    f = 0
  elif type(numb) != int:
    print "This is not a number"
 elif numb > 9 or numb < 0:
    print "This is not a number"
  else:
    dict[numb]()