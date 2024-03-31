import time
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu')
def final():
    return render_template('menu.html')


@app.route('/menu/shop')
def shop():
    product_data = [
        {"name": "Шлем", "image": "images/shop/shlem.png", "price": 1000},
        {"name": "Шлем", "image": "images/shop/shlem.png", "price": 1000},
        {"name": "Шлем", "image": "images/shop/shlem2.png", "price": 2000},
        {"name": "Шлем", "image": "images/shop/shlem2.png", "price": 2000},
        {"name": "Броня", "image": "images/shop/bron.png", "price": 3000},
        {"name": "Броня", "image": "images/shop/bron.png", "price": 3000},
        {"name": "Броня", "image": "images/shop/bron2.png", "price": 4000},
        {"name": "Броня", "image": "images/shop/bron2.png", "price": 4000}
    ]
    return render_template('shop.html', products=product_data)


@app.route('/menu/clan')
def clan():
    return render_template('clan.html')


@app.route('/menu/shop/cart')
def cart():
    return render_template('cart.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
