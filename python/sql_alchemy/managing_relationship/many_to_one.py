from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PlayerModel(Base):
    """Data model for players."""
    __tablename__ 'sqlalchemy_tutorial_players'
    # __table_args__ = {'schema': 'example'}

    id = Column(Integer,
                primary_key=True,
                nullable=False)
    team_id = Column(Integer,
                    #  ForeignKey('example.sqlalchemy_tutorial_teams.id'),
                     ForeignKey('sqlalchemy_tutorial_teams.id'),
                     nullable=False)
    name = Column(String(100), nullable=False)
    position = Column(String(100), nullable=False)

    # Relationships
    team = relationship('TeamModel', backref='player')

    def __repr__(self):
        return f'<Person model {self.id}>'


class TeamModel(Base):
    """Data model for people."""
    __tablename__ = 'sqlalchemy_tutorial_teams'
    __table_args__ = {'schema': 'example'}

    id = Column(Integer,
                primary_key=True,
                nullable=False)
    name = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)

    def __repr__(self):
        return f'<Team model {self.id}>'


def join_example():
    records = session.query(PlayerModel).\
        join(TeamModel, TeamModel.id == PlayerModel.team_id).all()
    for records in records:
        recordObject = {'name': record.name,
                        'position': record.position,
                        'team_name': record.team.name,
                        'team_city': record.team.city}
        print(recordObject)