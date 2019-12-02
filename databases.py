from model import Base, Product, Cart
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///database.db')
# Base.metadata.create_all(engine)
# DBSession = sessionmaker(bind=engine)
# session = DBSession()


def createThread():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session


def add_product(session, name, price, pic_link, description):

	product = Product(name=name, price=price, pic_link=pic_link, description=description)
	session.add(product)
	session.commit()


def edit_product(session, ID, name, price, pic_link, description):

	product = session.query(Product).filter_by(ID=ID)

	product.name = name
	product.price = price
	product.pic_link = pic_link
	product.description = description

	session.commit()


def edit_img_link(session, name):

	product = session.query(Product).filter_by(name=name).first()

def delete_product(session, ID):

	session.query(Product).filter_by(ID=ID).first().delete()
	session.commit()


def all_products(session):

	return session.query(Product).all()


def get_product(session, ID):

	return session.query(Product).filter_by(ID=ID)


def add_to_cart(session, productID):

	item = Cart(productID = productID)
	session.add(item)
	session.commit()

def get_cart_items(session):

	return session.query(Cart).all()

def get_products(session, prodList):

	cartList = list()

	for productID in prodList:
		cartList.append(get_product(createThread(), productID))

	return cartList


# add_product(createThread(), "Black Pen", 20, "blackPen.png", "This pen is very black")
# add_product(createThread(), "Blue Pen", 12.5, "bluePen.jpg", "A very blue pen")
# add_product(createThread(), "Red Pen", 15, "redPen.jpg", "In case you want a red pen")
# add_product(createThread(), "Green Pen", 30, "greenPen.jpg", "It is a green pen")



# products = get_cart_items(createThread())

# for p in products:
# 	print("name: " + p.name)
# 	print("price: " + str(p.price))
# 	print("pic_link: " + p.pic_link)
# 	print("description: " + p.description)
# 	print()

# edit_img_link()