from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_username = "postgres"
db_password = "postgres"
db_url = "127.0.0.1:5432"
db_name = "postgres"

connectionString = f'postgresql+pymysql://{db_username}:{db_password}@{db_url}/{db_name}'

# use echo=True for debugging
engine = create_engine(connectionString, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()