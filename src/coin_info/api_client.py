
import requests
from config import Api
import json
from utils import NullToNoneDecoder


def get_new_info():
    url = Api.URL_NEW_INFO
    headers = {
        'X-CMC_PRO_API_KEY': Api.SECRET,
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # 使用自定義解碼器將 null 轉換為 None
            return json.loads(response.text, cls=NullToNoneDecoder)
        else:
            print(f"Error calling API, status code: {response.status_code}")
            return None
    except Exception as error:
        print(f"Error during API call: {error}")
        return None
