import tornado.ioloop
import tornado.web
from handlers import home
from tornado.options import define, options, parse_command_line


define("port", default="8000", help="Listening port", type=int)


def make_app():
    return tornado.web.Application(
        debug=True,
        handlers=[
            (r"/", home.HomeHandler),
        ],
    )


if __name__ == "__main__":
    parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
