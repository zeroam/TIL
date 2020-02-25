from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('team_id', Integer, ForeignKey('example.sqlalchemy_tutorial_players.team_id')),
    Column('id', Integer, ForeignKey('example.sqlalchemy_tutorial_teams.id'))
)


class PlayerModel(Base):
    """Data model for players."""
    __tablename__ = 'sqlalchemy_tutorial_players'
    __table_args__ = {'schema': 'example'}

    id = Column(Integer,
                primary_key=True,
                unique=True,
                nullable=False)
    team_id = Column(Integer,
                     ForeignKey('example.sqlalchemy_tutorial_teams.id'),
                     nullable=False)
    name = Column(String(100), nullable=False)
    position = Column(String(100), nullable=False)
    
    # Relationships
    teams = relationship('TeamModel',
                         secondary=association_table,
                         backref='player')

    def __repr__(self):
        return f'<Player model {self.id}>'


class TeamModel(Base):
    """Data model for people."""
    __tablename__ = 'sqlalchemy_tutorial_teams'
    __table_args__ = {'schema': 'example'}

    id = Column(Integer,
                primary_key=True,
                unique=True,
                nullable=False)
    name = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)

    def __repr__(self):
        return f'<Team model {self.id}>'

                     