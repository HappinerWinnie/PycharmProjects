import tornado.web

class loginHandler(tornado.web.RequestHandler):
    # override
    def initialize(self, name, age):
        self.name = name
        self.age = age
    # override
    def get(self, *args, **kwargs):
        print(self.name, self.age)
        self.write("login")  # Django HttpResponse

    def post(self, *args, **kwargs):
        pass
