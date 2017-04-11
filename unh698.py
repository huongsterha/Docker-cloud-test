from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'UNH698 Website'

if __name__== '_main_':
	port = int(ubuntu.environ.get('PORT', 5000))

	if port == 5000:
		app.debug = True

	app.run(host='0.0.0.0', port=port)
