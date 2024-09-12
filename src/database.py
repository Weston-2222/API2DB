from sqlalchemy.orm import sessionmaker
from config import DB
from sqlalchemy import create_engine, inspect
# 初始化数据库連結:

# 判断是否在 Google Cloud 环境中运行
if DB.is_production:
    # 在 Google Cloud 环境中使用 Unix 套接字
    connection_string = f'postgresql+psycopg2://{DB.USER}:{DB.PASSWORD}@{DB.IP}:{DB.PORT}/{DB.NAME}?host=/cloudsql/{DB.CLOUD_SQL_CONNECTION_NAME}'
else:
    # 在本地开发环境中使用 TCP 连接
    connection_string = f'postgresql+psycopg2://{DB.USER}:{DB.PASSWORD}@{DB.IP}:{DB.PORT}/{DB.NAME}'

engine = create_engine(connection_string)
DBSession = sessionmaker(bind=engine)


def get_session():
    # 返回一個新的資料庫會話(session)。
    return DBSession()


if __name__ == "__main__":
    try:
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print("数据库中的表：", tables)
        print("连接成功")
    except Exception as e:
        print(f"連接失敗：{str(e)}")
