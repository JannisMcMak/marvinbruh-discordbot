from random import randint
import json
import sys

async def bitchass(i):
  switcher={
    1:'{} is a little bitch ass bitch bitch why so dumb hahah stupid hahah dumb {} lmao bitch ass bitch hahah small cock no balls bitch ass bitch',
    2:'{} is a little bitch ass bitch bitch why so dumb hahah stupid hahah dumb {} lmao bitch ass bitch hahah small cock no balls bitch ass bitch bitch bitch bitch bitch bitch ok again bitch bitch bich bitch bitch lmao',
    3:'{} is a little bitch ass bitch bitch why so dumb hahah stupid hahah dumb {} lmao bitch ass bitch hahah small cock no balls bitch ass bitch bitch bitch bitch bitch bitch ok again bitch bitch bich bitch bitch lmao {} is so dumb hahah such a bitch look at him lmao haha bitch ass bitch bitch',
    4:'{} is a little bitch ass bitch bitch why so dumb hahah stupid hahah dumb {} lmao bitch ass bitch hahah small cock no balls bitch ass bitch bitch bitch bitch bitch bitch ok again bitch bitch bich bitch bitch lmao {} is so dumb hahah such a bitch look at him lmao haha bitch ass bitch bitch u are such a bitch lmao i cant believe how fucking stupid you are bitch ass bitch stop existing you bitch ass bitch hahaahh bitch lmao bitch i hate you your life is a bruh momentum just like mine hahah lmao fuck you {} stupid bitch ass bitch bitch bitch',
    5:'{} is a little bitch ass bitch bitch why so dumb hahah stupid hahah dumb lmao bitch ass bitch hahah small cock no balls bitch ass bitch bitch bitch bitch bitch bitch ok again bitch bitch bich bitch bitch lmao {} is so dumb hahah such a bitch look at him lmao haha bitch ass bitch bitch u are such a bitch lmao i cant believe how fucking stupid you are bitch ass bitch stop existing you bitch ass bitch hahaahh bitch lmao bitch i hate you your life is a bruh momentum just like mine hahah lmao fuck you stupid bitch ass bitch bitch bitch imagine being {} hahah i cant believe how stupid this bitch is lmao hahahah its funny because he is so fucking dumb hahah bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch bitch lmao fuck you {} bitch ass bitch bitch'
  }
  return switcher.get(i, "{} is a little bitch")


async def poetry(i):
  with open('gedichte.json') as json_file:
    data = json.load(json_file)
    print(len(data))
    if i == 0:
      i = randint(1, len(data))
    
    print(i)

    return data.get(str(i), 'Kein Gedicht gefunden...')


async def count(command):
  filename = 'counter/' + command + '.txt'
  print(filename)
  f = open(filename, 'r')
  try:
    count = f.read()
  except:
    print(sys.exc_info()[0])
    raise
  finally:
    f.close()
  print(count)
  g = open(filename, 'w')
  try:
    g.write(str(int(count) + 1))
  except:
    print(sys.exc_info()[0])
    raise
  finally:
    g.close()

async def get_counters():
  counters = ['versuh', 'bitch', 'gedicht', 'mp3s']
  values = []
  for c in counters:
    f = open('counter/' + c + '.txt', 'r')
    values.append(f.read())
  
  return counters, values



