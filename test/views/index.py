import tornado.web


class statusHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        #self.set_status(666, "this is 666 status")
        #self.set_status(404, "this is 666 status")
        #self.write("status")

        #反向解析 别名为 myurl的路由
        #url = self.reverse_url("myurl")
        #print(url)
        #self.write("<a href = '%s'>跳转到url</a>"%(url))
        #self.redirect(url)
        #self.render("../templates/status.html")
        self.render("status.html")