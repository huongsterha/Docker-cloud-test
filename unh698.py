from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')
    
@app.route('/Coffee')
def coffee():
    return render_template('coffee.html')
    
@app.route('/coffeeInfo')
def linktocoffee():
    return render_template('decafCoffee.html')

if __name__== '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)
