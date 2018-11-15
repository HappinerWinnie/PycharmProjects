import os
import tornado.ioloop
import tornado.httpserver
from application import Application

import config

if __name__ == "__main__":
    app = Application()

    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(config.options.get("port"))
    httpServer.start()  # 如果传入的参数为None 或者小于等于0，开启对应cpu核心数个子进程

    tornado.ioloop.IOLoop.current().start()