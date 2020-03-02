""" Example from 
https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#one-to-many
"""
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""One to Many
Parent : Child = 1 : N
"""
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship('Child', back_populates='parent')

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship('Parent', back_populates='children')


"""Many To One
Parent : Child = N : 1
"""
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey=True)
    child = relationship('Child', back_populates='parents')

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parents = relationship('Parent', back_populates='child')


"""One To One
Parnet : Child = 1 : 1
"""
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    child = relationship('Child', uselist=False, back_popultes='parent')

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship('Parent', back_populates='child')


"""Many To Many
Parent : Child = M : N
"""
association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship(
        'Child',
        secondary=association_table,
        back_populates='parents')

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
    parents = relationship(
        'Parent',
        secondary=association_table,
        back_populates='children'
    )


"""Association Object
"""
class Association(Base):
    __tablename__ = 'association'
    left_id = Column(Integer, ForeignKey('left.id'), primary_key=True)
    right_id = Column(Integer, ForeignKey('right.id'), primary_key=True)
    extra_data = Column(String(50))
    child = relationship('Child', back_populates='parents')
    parent = relationship('Parent', back_populates='children')

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship('Association', back_populates='parent')

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
    parents = relationship('Association', back_populates='child')
