from flask import Flask, send_file
import threading
import time
import requests

app = Flask(__name__)

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
#FLASK
@app.route('/get_proxy', methods=['GET'])
def get_proxy_route():
    try:
        file_path = 'proxy.txt'
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return str(e)

flask_thread = threading.Thread(target=app.run, kwargs={'debug': False})
main_thread = threading.Thread(target=main)
if __name__ == '__main__':
    flask_thread.start()
    main_thread.start()
