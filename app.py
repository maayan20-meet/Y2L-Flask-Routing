from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"
app.config['SECRET_KEY'] = app.secret_key

ADMIN_USERNAME = 'maayan'
ADMIN_PASSWORD = 'password'

login_session['is_admin'] = False

@app.route('/')
def home():
	return render_template('home.html')

# @app.route('/admin')
# def home():
# 	return render_template('admin.html')

@app.route('/store')
def store():

	return render_template('store.html', products=all_products(createThread()))

@app.route('/addToCart/<string:prodID>')
def addToCart(prodID):

	if prodID is not None:
		add_to_cart(createThread(), int(prodID))

	return redirect(url_for('cart'))

@app.route('/cart')
def cart():

	products = get_products(get_cart_items(createThread()))

	return render_template('cart.html', products=products)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/pay')
def pay():

	delete_all_items(createThread())
	return redirect(url_for('cart'))

@app.route('/login', methods=['POST'])
def login:

	if request.form['username'] is ADMIN_USERNAME and request.form['username'] is ADMIN_PASSWORD:
		login_session['is_admin'] = True
		return redirect(url_for('portal'))

@app.route('/portal')
def portal():

	if login_session['is_admin'] is False:
		return 'You are not an admin :3'

	return render_template('portal.html', products=get_products(createThread()))

@app.route('edit/<string:prodID>', methods = ['GET', 'POST'])
def edit(prodID):
	if login_session['is_admin'] is False:
		return 'You are not an admin :3'

	elif request.method is 'GET':
		return render_template('edit.html', prodID = prodID)

	edit_product(createThread(), prodID, request.form['name'],  request.form['price'],  request.form['description'])
	return redirect(url_for('portal'))

if __name__ == '__main__':
    app.run(debug=True)