from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


# from security import authenticate, identity
# from resources.user import UserRegister
# from resources.customer import Customer
# from resources.service import Service, ServiceItem
# from resources.vehicle import Vehicle
# from resources.brand import Brand
# from resources.model import Model


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'any_you_may_like'
api = Api(app)

# jwt = JWT(app, authenticate, identity)

# api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debut=True)