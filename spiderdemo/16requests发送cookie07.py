import requests
url = 'http://127.0.0.1:8000/admin/'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
             "Chrome/66.0.3359.181 Safari/537.36"
}
cookies = dict(
    csrftoken = 'wCbDeanCee85cS37SJYNet1X1oehTx80H1tljTP',
    sessionid = 'mgsxclcr7bafi61bmjuw2820orws4aw8'
)
resp = requests.get(url, headers, cookies=cookies)
print(resp.text)
