from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.sql.sqltypes import FLOAT
from sqlalchemy.sql.sqltypes import INT
from sqlalchemy.sql.sqltypes import ARRAY

Base = declarative_base()

class Release(Base):
    __tablename__ = 'wantlist_data'
    id = Column(INT, primary_key=True)
    title = Column(String)
    artists = Column(ARRAY(String))
    formats = Column(ARRAY(String))
    num_for_sale = Column(INT)
    lowest_price = Column(FLOAT)