from datetime import datetime, timedelta
from config import News
import requests


def fetch_news():
    # three_hours_ago = datetime.now() - timedelta(hours=3)
    # formatted_time = three_hours_ago.strftime(
    #     '%Y-%m-%dT%H:%M:%S.%f')[:-3] + three_hours_ago.strftime('%z')
    params = {
        "language": 'zh',
        "apiKey": News.API_KEY,
        "category": "technology",
        # "start_date": formatted_time
    }

    url = f"{News.API_URL}"
    try:
        response = requests.get(url, params)
        if response.status_code == 200:
            # 使用自定義解碼器將 null 轉換為 None
            data = response.json()

            return data['news']
        else:
            print(f"Error calling API, status code: {response.status_code}")
            return None
    except Exception as error:
        print(f"Error during API call: {error}")
        return None
