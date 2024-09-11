from sqlalchemy.dialects.postgresql import insert
from coin_info.models import CoinInfoModel


def upsert_many_coin_info(session, data):
    # 構建 UPSERT 操作
    insert_stmt = insert(CoinInfoModel).values(data)
    upsert_stmt = insert_stmt.on_conflict_do_update(
        index_elements=['id'],  # 唯一索引的列
        set_={'cmc_rank': insert_stmt.excluded.cmc_rank,
              "circulating_supply": insert_stmt.excluded.circulating_supply,
              "total_supply": insert_stmt.excluded.total_supply,
              "max_supply": insert_stmt.excluded.max_supply,
              "infinite_supply": insert_stmt.excluded.infinite_supply,
              "price": insert_stmt.excluded.price,
              "volume_change_24h": insert_stmt.excluded.volume_change_24h,
              "percent_change_1h": insert_stmt.excluded.percent_change_1h,
              "percent_change_24h": insert_stmt.excluded.percent_change_24h,
              "percent_change_7d": insert_stmt.excluded.percent_change_7d,
              "market_cap": insert_stmt.excluded.market_cap,
              "market_cap_dominance": insert_stmt.excluded.market_cap_dominance,
              "fully_diluted_market_cap": insert_stmt.excluded.fully_diluted_market_cap,
              "last_updated": insert_stmt.excluded.last_updated}  # 更新列
    )

    # 執行操作
    session.execute(upsert_stmt)
