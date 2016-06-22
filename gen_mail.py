import random
import string

def random_f(length):
  rid = ""
  for x in range(length):
      rid += random.choice(string.ascii_letters + string.digits)
  return rid

def mail():
    a= random_f(5)
    b= random_f(3)
    c = a+"@"+b+"."
    return c
im=1
while im<25:
  for i in ["nl","no","np","su","sv","sy","sz","tc","td","tf","tg","th","tj","tk","tl","tm","tn","to","cz","com","ru"]:
    print (mail()+i)
    im=im+1
