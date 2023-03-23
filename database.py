""" 
该文件将负责创建数据库并定义模型类。由于数据访问部分被封装到了 MarkerService 中，因此这里只需要定义模型类：
"""
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///marker.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Marker(Base):
    __tablename__ = 'marker'

    id = Column(Integer, primary_key=True , nullable=False)
    content = Column(String)
    name = Column(String)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    star = Column(Integer)
    kind = Column(String)


    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_')}

    def to_dict_with_id(self):
        return {
            'id': self.id,
            **self.to_dict()
        }

Base.metadata.create_all(engine)
