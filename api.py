from flask import Flask
from models import setup_db, db
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__)

    CORS(app)

    setup_db(app)

    @app.route('/api/hello')
    def say_hello():
        return 'Hi!'

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
