from sqlalchemy.dialects.postgresql import insert

from database import get_session
from news.api_client import fetch_news
from news.models import NewsModel, newsTransform
import logging
# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def upsert_many_news(session, data):
    # 構建 UPSERT 操作

    insert_stmt = insert(NewsModel).values(data)
    upsert_stmt = insert_stmt.on_conflict_do_nothing(
        index_elements=['id'],  # 唯一索引的列
    )

    # 執行操作
    session.execute(upsert_stmt)


def update_news():
    try:
        logger.info("开始更新新聞数据")
        # 取得資料
        json_data = fetch_news()

        logger.info("成功获取新聞数据")

        # 將data轉換為DataBase需要的格式
        news = newsTransform(json_data)
        logger.info("新聞数据转换完成")

        # 取得session
        session = get_session()
        try:
            # 將資料寫入資料庫
            upsert_many_news(session, news)
            # 提交
            session.commit()
            logger.info("新聞数据成功写入数据库")
        except Exception as e:
            session.rollback()
            logger.error(f"新聞数据库操作错误：{str(e)}")
        finally:
            # 關閉session
            session.close()
            logger.info("新聞數據庫会话已關閉")

    except Exception as e:
        logger.error(f"新聞更新过程中發生错误：{str(e)}")
