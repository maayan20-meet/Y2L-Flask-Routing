from model import Base, Product
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_product(name, price, pic_link, description):

	product = Product(name=name, price=price, pic_link=pic_link, description=description)
	session.add(product)
	session.commit()


def edit_product(ID, name, price, pic_link, description):

	product = session.query(Product).filter_by(ID=ID).first()

	product.name = name
	product.price = price
	product.pic_link = pic_link
	product.description = description


def delete_product(ID):

	session.query(Product).filter_by(ID=ID).first().delete()
	session.commit()


def all_products():

	return session.query(Product).all()


def get_product(ID):

	return session.query(Product).filter_by(ID=ID).first()


def add_to_cart(productID):

	item = Cart(productID = productID)
	session.add(item)
	session.commit()

# add_product("Black Pen", 20, "resources/blackPen.png", "This pen is very black")
# add_product("Blue Pen", 12.5, "resources/bluePen.jpg", "A very blue pen")
# add_product("Red Pen", 15, "resources/redPen.jpg", "In case you want a red pen")
# add_product("Green Pen", 30, "resources/greenPen.png", "It is a green pen")


# products = all_products()

# for p in products:
# 	print("name: " + p.name)
# 	print("price: " + str(p.price))
# 	print("pic_link: " + p.pic_link)
# 	print("description: " + p.description)
# 	print()