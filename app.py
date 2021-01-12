from flask import Flask
from requests import get

app = Flask('__main__')
SITE_NAME = 'https://cuongmx.medium.com/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  return get(f'{SITE_NAME}{path}').content