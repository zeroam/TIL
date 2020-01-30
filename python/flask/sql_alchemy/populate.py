from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Book, Base

engine = create_engine('sqlite:///books-collection.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object
session = DBSession()

# CREATE
bookOne = Book(title="The Bell Jar", author="Sylvia Pla", genre="roman a clef")
session.add(bookOne)
session.commit()

# READ
book_list = session.query(Book).all()
book_one = session.query(Book).first()
print(f'book_list: {book_list}')
print(f'book_one: {book_one}')

# UPDATE
edited_book = session.query(Book).filter_by(id=1).one()
edited_book.author = 'Sylvia Plath'
session.add(edited_book)
session.commit()

book_list = session.query(Book).all()
print(f'book_list: {book_list}')

# DELETE
book_to_delete = session.query(Book).filter_by(title='The Bell Jar').one()
session.delete(book_to_delete)
session.commit()

book_list = session.query(Book).all()
print(f'book_list: {book_list}')