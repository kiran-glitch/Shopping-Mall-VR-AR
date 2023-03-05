from flask import Flask, request, jsonify, render_template ,  send_from_directory
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/product')
def product():
    return render_template('/products.html')


@app.route('/cart')
def cart():
    return render_template('/cart.html')

@app.route('/tshirt')
def tshirt():
    return render_template('/t-shirt.html')

@app.route('/pinktshirt')
def pinktshirt():
    return render_template('/pinktshirt.html')

@app.route('/reddress')
def reddress():
    return render_template('/reddress.html')

@app.route('/partydress')
def partydress():
    return render_template('/partydress.html')

@app.route('/blackdress')
def blackdress():
    return render_template('/blackdress.html')

@app.route('/yellowdress')
def yellowdress():
    return render_template('/yellowdress.html')

@app.route('/waterdress')
def waterdress():
    return render_template('/waterdress.html')

@app.route('/bluedress')
def bluedress():
    return render_template('/bluedress.html')

@app.route('/darkbluedress')
def darkbluedress():
    return render_template('/darkbluedress.html')

@app.route('/sofac')
def sofac():
    return render_template('/sofac.html')

@app.route('/tablesofa')
def tablesofa():
    return render_template('/tablesofa.html')

@app.route('/sofa')
def sofa():
    return render_template('/sofa.html')

@app.route('/dinningtable')
def dinningtable():
    return render_template('/dinningtable.html')

@app.route('/glasstable')
def glasstable():
    return render_template('/glasstable.html')

if __name__ == '__main__':
    app.run()
