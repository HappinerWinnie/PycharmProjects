import tornado.web

import json

class indexHandler(tornado.web.RequestHandler):
    # override
    def get(self, *args, **kwargs):
        #self.write("hello")  # Django HttpResponse
        data = {
            "name":"zhangsan",
            "age":18
        }

        list = ["zhangsan", "lisi", "wangwu"]
        #data_str = json.dumps(data)
        #self.write(data_str)
        #TypeError: write() only accepts bytes, unicode, and dict objects. Lists not accepted for security reasons;
        data_str = json.dumps(list)
        self.write(data_str)

    def post(self, *args, **kwargs):
        pass


class requestHandler(tornado.web.RequestHandler):
    def get(self, *args,**kwargs):
        # print(type(self.request))
        # print(self.request.protocol)
        # print(self.request.host)
        # print(self.request.method)
        # print(self.request.uri)
        # print(self.request.path)
        # print(self.request.remote_ip)

        #获取get请求的参数
        # ret = self.get_query_argument("user", default="abc", strip=True)
        # print(ret)

        ret = self.get_query_arguments("user",strip=True)
        print(ret[0], ret[1])

        self.write("hello")

class statusHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        #self.set_status(666, "this is 666 status")
        #self.set_status(404, "this is 666 status")
        #self.write("status")

        #反向解析 别名为 myurl的路由
        url = self.reverse_url("myurl")
        print(url)
        #self.write("<a href = '%s'>跳转到url</a>"%(url))
        #self.redirect(url)
        #self.render("../templates/index.html")
        self.render("index.html")

class urlHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("myurl")