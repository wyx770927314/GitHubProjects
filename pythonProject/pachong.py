import ssl
import requests
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context


# 获取15个免费ip
def get_free_ip():
    iplist = []
    params = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }
    response = requests.get(url='https://www.kuaidaili.com/free/inha/2/', params=params)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    for row in soup.tbody.find_all('tr')[0:]:
        # print(row.td.text)
        iplist.append(row.td.text)
    return iplist


# 设置代理池
def set_proxy():
    list_ip = get_free_ip()
    proxy = list_ip[0]
    print(proxy)
    print(type(proxy))
    proxies = {
        'http': 'http://' + proxy + ':9743',
        'https': 'https://' + proxy + ':9743',
    }
    try:
        response = requests.get('http://www.httpbin.org/get', proxies=proxies)
        print(response.text)
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)


if __name__ == '__main__':
    set_proxy()
