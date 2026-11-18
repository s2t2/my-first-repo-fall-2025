# this is the "web_app/__init__.py" file...
# it acts as the entry point for the web_app directory
# later when we tell flask to go run an app that has been defined
# in the web_app directory, it's going to look here first
# and execute this code to run the app in our browser

from flask import Flask

from web_app.routes.home_routes import home_routes
#from web_app.routes.book_routes import book_routes
#from web_app.routes.weather_routes import weather_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    #app.register_blueprint(book_routes)
    #app.register_blueprint(weather_routes)
    return app

if __name__ == "__main__":
    # when you run this from the command line, the following code will be executed
    my_app = create_app()
    my_app.run(debug=True)