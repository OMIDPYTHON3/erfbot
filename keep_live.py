from flask import Flask,render_template
from threading import Thread

app2 = Flask(__name__)

@app2.route('/on')
def index():
    return "Alive"

def run():
  app2.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()