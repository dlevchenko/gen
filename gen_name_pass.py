import random
import string


q=35
i=0
while i<10:
    while i <q:
        def random_id():
          rid = ""
          for x in range(random.randint(1, 25)):
              rid += random.choice(string.ascii_letters + string.digits)
          return rid
        print (random_id())
        i=i+1
