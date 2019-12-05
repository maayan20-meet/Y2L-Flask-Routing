from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"
app.config['SECRET_KEY'] = app.secret_key

@app.route('/')
def home():
	return render_template('home.html')

# @app.route('/admin')
# def home():
# 	return render_template('admin.html')

@app.route('/store')
def store():
	return render_template('store.html', products=all_products(createThread()))

@app.route('/cart')
def noneCart():
	return cart(None)


@app.route('/cart/<string:prodID>')
def cart(prodID):
	if prodID is not None:
		print(prodID)
		add_to_cart(createThread(), int(prodID))

	products = get_products(get_cart_items(createThread()))
	for i in products:
		printProduct(i)

	return render_template('cart.html', products=products)


@app.route('/about')
def about():
	return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)