import tornado.ioloop
import tornado.httpserver
import config
from application import Application

if __name__ == '__main__':

    app = Application()
    print(__file__)
    httpserver = tornado.httpserver.HTTPServer(app)
    httpserver.bind(config.options.get("port"))
    #httpserver.bind(8888)
    httpserver.start()  # 默认是创建和cpu的核心数个数一致的子进程
    #IOLoop IO循环的类：内部继承了epoll实现高并发
    tornado.ioloop.IOLoop.current().start()