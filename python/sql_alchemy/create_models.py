from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy.types import Integer, Text, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    fullname = Column(String(120), unique=True, nullable=False)
    nickname = Column(String(120), unique=True, nullable=False)
    # username = Column(String(80), unique=True, nullable=False)
    # email = Column(String(120), unique=True, nullable=False)
    # joined = Column(DateTime, unique=False, nullable=False)

    # cascade configuration
    addresses = relationship('Address', back_populates='user',
                             cascade='all, delete, delete-orphan')
    
    def __repr__(self):
        return f"<User (name='{self.name}', fullname='{self.fullname}', nickname='{self.nickname}')>"


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='addresses')

    def __repr__(self):
        return f"<Address(email_address='{self.email_address}')>"


# User.addresses = relationship(
#     'Address', order_by=Address.id, back_populates='user'
# )

"""Building a Many To Many Relationship"""
from sqlalchemy import Table, Text
# association table
post_keywords = Table('post_keywords', Base.metadata,
    Column('post_id', ForeignKey('posts.id'), primary_key=True),
    Column('keyword_id', ForeignKey('keywords.id'), primary_key=True)
) 


class BlogPost(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    headline = Column(String(255), nullable=True)
    body = Column(Text)

    # many to many BlogPost <-> Keyword
    keywords = relationship('Keyword',
                            secondary=post_keywords,
                            back_populates='posts')

    def __init__(self, headline, body, author):
        self.author = author
        self.headline = headline
        self.body = body

    def __repr__(self):
        return f'BlogPost({self.headline}, {self.body}, {self.author})'


class Keyword(Base):
    __tablename__ = 'keywords'

    id = Column(Integer, primary_key=True)
    keyword = Column(String(50), nullable=True, unique=True)
    posts = relationship('BlogPost',
                         secondary=post_keywords,
                         back_populates='keywords')

    def __init__(self, keyword):
        self.keyword = keyword


BlogPost.author = relationship(User, back_populates='posts')
User.posts = relationship(BlogPost, back_populates='author', lazy='dynamic')


if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:', echo=True)

    # initialize database
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # add data to database
    jack = User(name='jack', fullname='Jack Bean', nickname='gjffdd')
    jack.addresses = [
        Address(email_address='jack@google.com'),
        Address(email_address='j25@yahoo.com')
    ]
    session.add(jack)
    session.commit()

    # many to many
    wendy = User(name='wendy', fullname='Wendy', nickname='sadfj')
    session.add(wendy)

    post = BlogPost("Wendy's Blog Post", "This is a test", wendy)
    post.keywords.append(Keyword('wendy'))
    post.keywords.append(Keyword('firstpost'))
    session.add(post)

    session.commit()
