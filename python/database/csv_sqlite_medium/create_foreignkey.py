from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')

    def __repr__(self): # optional
        return f'Product {self.name}'


class User(Base):
    __tablename__ = 'user'  # if you use base it is obligatory

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    products = relationship(Product, backref='users')

    def __repr__(self): # optional
        return f'User {self.name}'


def start():
    engine = create_engine('sqlite:///:memory:', echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    return engine, session


if __name__ == '__main__':
    engine, session = start()

    user = User(name='John')
    product = Product(name='wolf', user=user)

    session.add_all([user, product])
    session.commit()