from sqlalchemy import *

engine = create_engine('mysql+pymysql://root:root@localhost:3306/app')
metadata = MetaData()

user = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20), nullable=False),
    Column('email', String(20)),
    Column('password', String(20), nullable=False),
    Column('status', String(10)),
    Column('created_at', Date)
)
