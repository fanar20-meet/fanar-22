from model import Base,User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session

engine = create_engine('sqlite:///students.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))


def add_user(name, year,num):
	user_object = User(
		name=name,
		year=year,
		num=num
		)
	session.add(user_object)
	session.commit()



def query_all():

	users = session.query(User).all()
	return users

def query_by_name(name):
    user = session.query(User).filter_by(
        name=name).first()
    return user


def query_by_id(user_id):
    user = session.query(User).filter_by(
        user_id=user_id).first()
    return user


def plusone():
	if button1.isPressed():
		query_by_name(name).num +=1 

		