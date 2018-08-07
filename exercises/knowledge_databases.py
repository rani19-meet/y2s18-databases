from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(article_title,topic_of_article,rating_of_article):
	insert_object= Knowledge(
		article_title=article_title,
		topic_of_article=topic_of_article,
		rating_of_article=rating_of_article)
	session.add(insert_object)
	session.commit()
	
add_article("meet","hthr",9)


def query_all_articles():
	jon = session.query(Knowledge).all()
	return jon
#print(query_all_articles())


def query_article_by_topic(topic_of_article):
	jon=session.query(Knowledge).filter_by(topic_of_article=topic_of_article).all()
	return jon

print(query_article_by_topic("hthr"))


def delete_article_by_topic(topic_of_article):
	jon = session.query(Knowledge).filter_by(topic_of_article=topic_of_article).delete()
	return jon
	session.commit()
delete_article_by_topic("hthr")
print(query_all_articles())


def delete_all_articles():
	jon = session.query(Knowledge).delete()
	return jon

delete_all_articles()
print(query_all_articles())


def edit_article_rating(rating_of_article,article_title):
	jon = session.query(Knowledge).filter_by(rating_of_article=rating_of_article,article_title=article_title).all()
	return jon
	session.commit()
edit_article_rating(10,"IASA")
print(query_all_articles())
