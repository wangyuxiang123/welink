import os
from datetime import datetime

import requests


class Do:
    def __init__(self):
        self.headers = {
            "Host": "wdk.chinasoftinc.com:18020",
            "Origin": "https://wdk.chinasoftinc.com:18020",
            "Content-Type": "application/json;charset=utf-8",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/HuaWei-AnyOffice/2.6.1802.0010/com.huawei.cloudlink.workplace",
            "Referer": "https://wdk.chinasoftinc.com:18020/daka/",
            "X-Requested-With": "XMLHttpRequest"
        }

    def punch(self, deviceId, openId):
        url = "https://wdk.chinasoftinc.com:18020/ehr_daka/icss/web/attEmpLog/saveAttEmpLog.welinkEmp?"
        check_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data = {
            "checkTime": check_time,
            "deviceId": deviceId,
            "longitude": 108.83895806206597,
            "checkType": 1,
            "verticalAccuracy": "30.00219079581817",
            "openId": openId,
            "latitude": 34.209211968315969,
            "type": 1,
            "altitude": "404.09",
            "versionCode": 58
        }

        response = requests.post(url, headers=self.headers, json=data)

        res_text = response.json()

        print("Status Code:", response.status_code)
        print("Response Body:", response.text)

        if res_text["msg"] == "打卡成功":
            print("打卡成功")
        else:
            print("打卡失败")


if __name__ == '__main__':
    deviceId = os.environ.get('DEVICEID', '')
    openId = os.environ.get('OPENID', '')
    uses = Do()
    uses.punch(deviceId, openId)
