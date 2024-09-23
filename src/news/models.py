from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class NewsModel(Base):
    __tablename__ = 'news'
    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    author = Column(String)
    image = Column(String)
    language = Column(String)
    published = Column(TIMESTAMP(timezone=True))


def newsTransform(data):
    def transform(item):
        return {
            "id": item['id'],
            "title": item['title'],
            "description": item['description'],
            "url": item['url'],
            "author": item['author'],
            "image": item['image'],
            "language": item['language'],
            "published": item['published']
        }
    return [transform(item) for item in data]
