from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


class Comic(Base):
    __tablename__ = "comic"

    id = Column('comic_number', primary_key=True, unique=True)
    comic_title = Column('comic_title', Text(), unique=True)
    image_url = Column('image_url', Text(), unique=True)
    image_title = Column('image_title', Text())
    image_alt_text = Column('image_alt_text', Text())
