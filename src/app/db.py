import os

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
    Table,
    MetaData
)

from sqlalchemy.sql import func

from databases import Database

DATABASE_URL = os.environ.get('DATABASE_URL')

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("descirption", String(50)),
    Column("created_date", DateTime, default = func.now(), nullable = False)
    )

# databases Query builder
database = Database(DATABASE_URL)