import tornado.web
import config

from views import index, websocket

#Application 继承自 tornado.web.Application
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', index.indexHandler),
            (r'/websocket', websocket.websocketHandler)
        ]
        # 调用父类的__init__方法，并且将handlers 传递过去
        super().__init__(handlers, **config.settings)