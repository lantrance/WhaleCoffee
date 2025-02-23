from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123654987sd dfsd s'

    from .views import views
    from .admin import admin
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') # localhost:5000/about-us
    app.register_blueprint(auth, url_prefix='/auth') # localhost:5000/auth/change-password
    app.register_blueprint(admin, url_prefix='/')


    
    return app
