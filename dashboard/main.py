from flask import Flask, render_template, request, session, redirect
from oauth import Oauth
import requests

url = 'https://marvinbruhbot.jannismcmak.repl.co{}'

app = Flask('')
app.config["SECRET_KEY"] = "marvinbruh123testasdf"

@app.route('/')
def root():
  return redirect('/login')

@app.route("/login")
def home():
	return render_template("index.html", url = Oauth.discord_login_url)

@app.route("/dashboard")
def login():
  code = request.args.get("code")

  at = Oauth.get_access_token(code)
  session["token"] = at

  user = Oauth.get_user_json(at)
  user_name, user_id = user.get("username"), user.get('id')



  voice_channels = get_voice_channels()

  session['voice_channels'] = voice_channels
  session['username'] = user_name

  session['user_id'] = user_id
  session['channel_index'] = 0

  print(session['user_id'])
  print('Channel index', session['channel_index'])


  return render_template('dashboard.html', username=user_name, voice_channels=session['voice_channels'])


@app.route('/tts/<lang>')
def tts(lang):
  text = request.args.get('text')
  

  if lang == 'bitch' or lang == 'bitcht':
    level = request.args.get('level')
    text = request.args.get('name')
    tts_request(lang, text, level)
  else:
    tts_request(lang, text)
  print(lang, text)
  return render_template('dashboard.html', username=session['username'], voice_channels=session['voice_channels'])


@app.route('/mp3/<name>')
def mp3(name):
  
  print('mp3:', name)

  mp3_request(name)

  return render_template('dashboard.html', username=session['username'], voice_channels=session['voice_channels'])

@app.route('/selectchannel')
def selectchannel():
  i = request.args.get('i')
  print(i)

  session['channel_index'] = i
  
  return 'selected'
  


def get_channel(user_id):
  channel = requests.get(url.format('/channel?id={}'.format(user_id)))
  print(channel.text)
  if channel.text == 'Error':
    return None
  else:
    return channel.text

def get_voice_channels():
  channels = requests.get(url.format('/voicechannels')).json()
  
  return channels

def tts_request(lang, text, level=None):
  params = {'id': session['user_id'], 'i': session['channel_index'], 'lang': lang, 'text': text, 'level': level}
  requests.get(url.format('/tts'), params=params)

def mp3_request(name):
  params = {'id': session['user_id'], 'i': session['channel_index'], 'name': name}
  requests.get(url.format('/mp3'), params=params)


app.run(host='0.0.0.0', port=8080)


