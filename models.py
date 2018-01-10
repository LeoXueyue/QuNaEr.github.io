# coding:utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Qunaer(Base):
    __tablename__ = 'qunaer'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    position = Column(String(255))
    heat = Column(String(255))
    address = Column(String(255))
    info = Column(Text)
    price = Column(String(255))
    monthly_sales = Column(String(255))
    quality=Column(String(255))
    img = Column(String(255))

    # def __init__(self, id, name, position, heat, address, info, price, monthly_sales, quality, img):
    #     self.id = id
    #     self.name = name
    #     self.position = position
    #     self.heat = heat
    #     self.address = address
    #     self.info = info
    #     self.price = price
    #     self.monthly_sales = monthly_sales
    #     self.quality=quality
    #     self.img = img

    def __repr__(self):
        return '<Qunaer %s>' % self.name

    __str__ = __repr__

engine=create_engine("mysql+pymysql://root:admin@localhost:3306/qiushi",connect_args={'charset':'utf8'})

# Base.metadata.create_all(engine)

DBSession=sessionmaker(bind=engine)

session=DBSession()