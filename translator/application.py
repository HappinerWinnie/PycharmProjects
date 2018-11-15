import tornado.web
import config

from views import index


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.indexHandler),
        ]

        super(Application, self).__init__(handlers, **config.settings)
        #self.db = sql.gecMysql(config.mysql['host'], config.mysql['user'], config.mysql['passwd'],config.mysql['dbName'])