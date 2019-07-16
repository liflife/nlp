import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class FaceMainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("face:Hello, world")


def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/face", FaceMainHandler)

    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print('ok')
    tornado.ioloop.IOLoop.current().start()
