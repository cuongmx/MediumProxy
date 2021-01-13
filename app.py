from flask import Flask,request,redirect,Response
import requests, os

app = Flask('__main__')
SITE_NAME = os.environ.get('SITE_NAME', 'https://cuongmx.medium.com/')
SITE_NEW = os.environ.get('SITE_NEW', 'https://m.cuong.mx/')

@app.route('/favicon.ico')
#@app.route('/_/batch', methods=['POST'])
def nothing():
  return "Nope"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['POST','GET', 'OPTION'])
def proxy(path):
  if request.method=='GET':
    resp = requests.get(f'{SITE_NAME}{path}')
  elif request.method=='POST':
    resp = requests.post(f'{SITE_NAME}{path}',data=request.data)
  else: #'OPTION'
    resp = requests.options(f'{SITE_NAME}{path}')
  excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
  headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
  headers.append(['Access-Control-Allow-Origin', '*'])
  response = Response(resp.content.decode('utf-8').replace(SITE_NAME, SITE_NEW), resp.status_code, headers)
  return response