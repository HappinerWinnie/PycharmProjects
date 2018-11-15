import tornado.web
import requests
import json

class indexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")
    def translate(self):
        fanyi_url = "https://fanyi.baidu.com/extendtrans"
        data = {
            "from": "zh",
            "to": "en",
            "query": "人民",
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36"
        }
        r = requests.post(fanyi_url, data=data, headers=headers)
        print(r.status_code)
        print(r.content.decode())
        content_str = str(r.content.decode())

        content_dict = json.loads(content_str)
        print(content_dict)
        print(content_dict["data"]["st_tag"][0])

    def post(self, *args, **kwargs):
        pass