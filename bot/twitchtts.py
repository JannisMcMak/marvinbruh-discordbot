import requests
import json
import time
  
async def write_mp3_twitch(text):
  text = ' '.join(text)

  l = get_bytes(text)
  print(l)
  if l >= 550:
    return None

  base_url = 'https://lazypy.ro/tts/proxy.php?service=Polly&voice=Brian&text={}'

  r = requests.post(base_url.format(text))
  print(r.text)
  j = json.loads(r.text)
  url = j["speak_url"]
  r = requests.get(url)

  filename = 'cache/{}.mp3'.format(time.time())
  open(filename, 'wb').write(r.content)

  return filename

async def write_mp3_twitch_fromtext(text):
  l = get_bytes(text)
  print(l)
  if l >= 550:
    return None

  base_url = 'https://lazypy.ro/tts/proxy.php?service=Polly&voice=Brian&text={}'

  r = requests.post(base_url.format(text))
  print(r.text)
  j = json.loads(r.text)
  url = j["speak_url"]
  r = requests.get(url)

  filename = 'cache/{}.mp3'.format(time.time())
  open(filename, 'wb').write(r.content)

  return filename

def get_bytes(t):
  return len(t.encode('utf-8'))