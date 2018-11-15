import tornado.web
from views import index, login

import config

#Application 继承自 tornado.web.Application
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.indexHandler),
            (r"/login", login.loginHandler, {"name":"zhangsan", "age":18}),
            (r"/request", index.requestHandler),
            (r"/status", index.statusHandler),
            (r"/myurlhaha", index.urlHandler),
            #给路径/myurlhaha 设置一个别名：myurl
            tornado.web.url(r"/myurlhaha", index.urlHandler, name="myurl")
        ]

        #调用父类的__init__方法，并且将handlers 传递过去
        super().__init__(handlers, **config.settings)