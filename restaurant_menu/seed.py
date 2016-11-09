from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

#bind Base
Base.metadata.bind = engine
#session make
DBSession = sessionmaker(bind=engine)
session = DBSession()

#insert new restaurant
myFirstRestaurant = Restaurant(name="Pizza Palace")
session.add(myFirstRestaurant)
session.commit()