from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base


engine =create_engine("sqlite:///taskmanager.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

#class Base (DeclarativeMeta):
#    pass