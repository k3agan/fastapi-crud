import os
from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = os.environ.get('DATABASE_URL')

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# databases Query builder
database = Database(DATABASE_URL)