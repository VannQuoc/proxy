import requests
import time

def get_proxy(web):
    response = requests.get(web)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return None
def main():
    while True:
        with open('http.txt', 'w') as file:
            file.write('')
        with open('list.txt', 'r') as file:
            urls = file.readlines()
        for url in urls:
            url = url.strip()
            proxy = get_proxy(url)
            if proxy:
                    with open('http.txt', 'a') as http_file:
                        http_file.write(f'{proxy}\n')
        with open('proxy.txt', 'w') as file:
            file.write('')
        with open('http.txt', "r") as input_file:
            proxies = input_file.read().splitlines()
        for proxy in proxies:
            if not proxy.strip():
                continue
            try:
                response = requests.get("http://google.com", proxies={"http": proxy, "https": proxy}, timeout=2)
                if response.status_code == 200:
                    with open('proxy.txt', 'a') as http_file:
                        http_file.write(f'{proxy}\n')
            except requests.RequestException:
                pass
        time.sleep(300)
if __name__ == "__main__":
    main()
