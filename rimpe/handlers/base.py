import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../templates/base.jade")
