from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CoinInfoModel(Base):
    __tablename__ = 'coin_info'  # 資料庫中的表名
    id = Column(Integer, primary_key=True)  # 主鍵
    name = Column(String)
    symbol = Column(String)
    cmc_rank = Column(Integer)
    circulating_supply = Column(Integer)
    total_supply = Column(Integer)
    max_supply = Column(Integer)
    infinite_supply = Column(Boolean)
    price = Column(Float)
    volume_change_24h = Column(Float)
    percent_change_1h = Column(Float)
    percent_change_24h = Column(Float)
    percent_change_7d = Column(Float)
    market_cap = Column(Integer)
    market_cap_dominance = Column(Float)
    fully_diluted_market_cap = Column(Integer)
    last_updated = Column(TIMESTAMP(timezone=True))


def coinInfoTransform(data):
    def transform(item):
        return {
            'id': item['id'],
            'name': item['name'],
            'symbol': item['symbol'],
            'cmc_rank': item['cmc_rank'],
            'circulating_supply': item['circulating_supply'],
            'total_supply': item['total_supply'],
            'max_supply': item['max_supply'],
            'infinite_supply': item['infinite_supply'],
            'price': item['quote']['USD']['price'],
            'volume_change_24h': item['quote']['USD']['volume_change_24h'],
            'percent_change_1h': item['quote']['USD']['percent_change_1h'],
            'percent_change_24h': item['quote']['USD']['percent_change_24h'],
            'percent_change_7d': item['quote']['USD']['percent_change_7d'],
            'market_cap': item['quote']['USD']['market_cap'],
            'market_cap_dominance': item['quote']['USD']['market_cap_dominance'],
            'fully_diluted_market_cap': item['quote']['USD']['fully_diluted_market_cap'],
            'last_updated': item['quote']['USD']['last_updated'],
        }
    return list(map(transform, data['data']))
