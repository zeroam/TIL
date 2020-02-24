from sqlalchemy import create_engine

# [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
engine = create_engine('sqlite:///:memory:', echo=True)


"""connectionless execution
results = engine.execute([YOUR_QUERY])
for row in results:
    ...
results.close()
"""


"""connections
connection = engine.connect()
result = connection.execute([YOUR_QUERY])
for row in result:
    ...
connection.close()
"""


"""sessions
"""
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()