import logging
from coin_info.api_client import get_new_info
from coin_info.models import coinInfoTransform
from coin_info.services import upsert_many_coin_info
from database import get_session
from flask import Flask
import os


# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# 创建 Flask 应用
app = Flask(__name__)


@app.route('/')
def get_data():
    logger.info("接收到数据更新请求")
    update_data()
    return "Coin Info Service is running!"


def update_data():
    try:
        logger.info("开始更新数据")
        # 取得資料
        json_data = get_new_info()
        logger.info("成功获取新数据")

        # 將data轉換為DataBase需要的格式
        coinInfo = coinInfoTransform(json_data)
        logger.info("数据转换完成")

        # 取得session
        session = get_session()
        try:
            # 將資料寫入資料庫
            upsert_many_coin_info(session, coinInfo)
            # 提交
            session.commit()
            logger.info("数据成功写入数据库")
        except Exception as e:
            session.rollback()
            logger.error(f"数据库操作错误：{str(e)}")
        finally:
            # 關閉session
            session.close()
            logger.info("數據庫会话已關閉")

    except Exception as e:
        logger.error(f"更新过程中發生错误：{str(e)}")


def main():
    PORT = int(os.getenv('PORT', 8080))
    logger.info(f"應用程序正在啟動，端口：{PORT}")
    # 运行 Flask 应用
    app.run(host='0.0.0.0', port=PORT)


if __name__ == "__main__":
    main()
