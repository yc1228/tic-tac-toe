import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Tic Tac Toe Artificial Intelligence Agent")


class MoveHandler(tornado.web.RequestHandler):
    def post(self):
        board = self.get_argument("body"),
        print(board)
        self.write(board)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/move", MoveHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()
