from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship

from base import Base
from movie import movie_actors_association


class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)

    movies = relationship(
        'Movie',
        secondary=movie_actors_association,
        back_populates='actors'
    )
    stuntman = relationship('Stuntman', uselist=False, back_populates='actor')
    contact_details = relationship('ContactDetails', back_populates='actor')

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
