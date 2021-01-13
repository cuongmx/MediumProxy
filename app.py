from flask import Flask,request,redirect,Response
import requests

app = Flask('__main__')
SITE_NAME = 'https://cuongmx.medium.com/'
SITE_NEW = 'https://mediumx.herokuapp.com/'

@app.route('/favicon.ico')
#@app.route('/_/batch', methods=['POST'])
def nothing():
  """
  docstring
  """
  return "Nope"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['POST','GET', 'OPTION'])
def proxy(path):
#  return get(f'{SITE_NAME}{path}', verify=False).content
  if request.method=='GET':
    resp = requests.get(f'{SITE_NAME}{path}')
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
    headers.append(['Access-Control-Allow-Origin', '*'])
    response = Response(resp.content.decode('utf-8').replace(SITE_NAME, SITE_NEW), resp.status_code, headers)
    return response
  elif request.method=='POST':
    resp = requests.post(f'{SITE_NAME}{path}',data=request.data)
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
    headers.append(['Access-Control-Allow-Origin', '*'])
    response = Response(resp.content.decode('utf-8').replace(SITE_NAME, SITE_NEW), resp.status_code, headers)
    return response