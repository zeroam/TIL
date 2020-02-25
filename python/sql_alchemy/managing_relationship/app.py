from os import environ
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from example_model import Base, ExampleModel

# Create engine
# db_uri = environ.get('SQLALCHEMY_DATABASE_URI')
db_uri = 'sqlite:///data.db'
engine = create_engine(db_uri, echo=True)

# Create All Tables
Base.metadata.create_all(engine)

# create session
Session = sessionmaker(bind=engine)
session = Session()

# Adding a Record
newModel = ExampleModel(name='todd',
                        description='im testing this',
                        vip=True,
                        join_date=datetime.now())
session.add(newModel)
session.commit()
print(newModel)