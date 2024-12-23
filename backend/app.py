from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# imports
from extensions import db
from models import User
from CRUD import crud_bp

def create_app():
    app = Flask(__name__)

    # database file
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # register
    app.register_blueprint(crud_bp)
    
    @app.route('/')
    def home():
        return 'a'
    
    return app

# main
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)