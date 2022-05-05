import sqlalchemy
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text, String, DateTime

mysql+pymysql://root:Formula1!@127.0.0.1:3306/mydatabase

db_uri = environ.get('SQLALCHEMY_DATABASE_URI')
self.engine = create_engine(db_uri, echo=True)

table_name = 'turnover'

'turnover'.to_sql(
    table_name,
    engine,
    if_exists='replace',
    index=False,
    chunksize=500,
    dtype={"channel": Text, "store_id": Integer,"date": DateTime, "total_stamps": Integer }
    )