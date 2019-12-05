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

@app.route('/cart/<string:prodID>')
def cart(prodID):
	if prodID is not None:
		print(prodID)
		add_to_cart(createThread(), int(prodID))

	return render_template('cart.html', products=get_products(createThread(), get_cart_items(createThread())).productID)


@app.route('/about')
def about():
	return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)