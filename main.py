import requests

def main(username):
    proxies = {
        "https": 'http://Seleblinova:L5m8GvH@191.101.148.127:45785',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    cookies = {
        'sessionid': 'working',
        'csrftocken': 'working'
    }

    response = requests.get(f'https://www.instagram.com/{username}/?__a=1', headers=headers, proxies=proxies)

    return response.text

print(main('siesdemayo'))

