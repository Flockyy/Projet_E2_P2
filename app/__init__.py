from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models.users import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes
    from .routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    # blueprint for prediction routes
    from .routes.prediction import prediction as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    # blueprint for main routes
    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app