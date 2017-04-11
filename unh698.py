from flask import Flask
import 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'UNH698 Website'

if __name__== '_main_':
	app.run(host='0.0.0.0', port=5000)
