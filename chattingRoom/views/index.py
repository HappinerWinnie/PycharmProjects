from tornado.web import RequestHandler

class indexHandler(RequestHandler):

    def get(self, *args, **kwargs):

        self.render("index.html")