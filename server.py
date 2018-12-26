from datetime import datetime
from tornado.escape import json_encode, json_decode
import tornado.ioloop
import tornado.web

from models import User
from connection import session

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # user = session.query(User).get(1)
        users = session.query(User).all()
        users_list = []
        for user in users:
            users_list.append(repr(user))
        self.write(json_encode(users_list))

    def post(self):
        body = json_decode(self.request.body)
        name = body.get('name')
        email = body.get('email')

        user = User(
            name=name,
            email=email,
            created_at=datetime.now()
        )
        session.add(user)
        session.commit()
        self.write(json_encode(repr(user)))

def repr(user: User) -> dict:
    user_repr = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'created_at': user.created_at.strftime("%Y-%m-%d %H:%M:%S")
    }
    return user_repr

def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        ], debug=True)

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
