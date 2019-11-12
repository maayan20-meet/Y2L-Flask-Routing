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