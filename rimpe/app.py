import tornado.ioloop
import tornado.web
from handlers import home


def make_app():
    return tornado.web.Application(
        debug=True,
        handlers=[
            (r"/", home.HomeHandler),
        ],
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
