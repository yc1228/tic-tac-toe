import tornado.ioloop
import tornado.web
import agent


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.set_header("Access-Control-Allow-Methods",
                        "GET, POST, PUT, PATCH, DELETE")


class MainHandler(BaseHandler):
    def get(self):
        self.write("Tic Tac Toe Artificial Intelligence Agent")


class MoveHandler(BaseHandler):
    def post(self):
        board = tornado.escape.json_decode(self.request.body)
        move = agent.Agent(board).next_move()
        self.write(tornado.escape.json_encode(move))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/move", MoveHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()
