import requests


def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    html = requests.get(url, headers=headers)
    if html.status_code == 200:
        html.encoding = 'utf-8'
        # 将网页源码编码改为utf-8
        return html.text
    else:
        return None