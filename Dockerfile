FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

# 安裝 Cloud SQL Auth Proxy
ADD https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 /cloud_sql_proxy
RUN chmod +x /cloud_sql_proxy

# 啟動腳本
RUN echo '#!/bin/bash\n\
/cloud_sql_proxy -instances=hip-myth-434806-d1:asia-east1:coin-info=tcp:5432 &\n\
python3 src/main.py' > /start.sh && chmod +x /start.sh

CMD ["/start.sh"]