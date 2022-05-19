import tornado.ioloop
import tornado.web
from handlers import base


def make_app():
    return tornado.web.Application(
        [
            (r"/", base.BaseHandler),
        ]
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
