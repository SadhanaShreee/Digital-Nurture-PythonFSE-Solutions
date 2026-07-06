from flask import Flask, jsonify
from config import Config
from flask_migrate import Migrate
from extensions import db

#db = SQLAlchemy() # having  a db as sqlalchemy object and not a temp list as in the previous hands-on

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app) # connects the outher db to this specific app instance
    migrate = Migrate(app,db) # enables all the flask db commands

    from courses import models

    from courses.routes import courses_bp
    app.register_blueprint(courses_bp)

    @app.errorhandler(404)
    def not_founded(e):
        return jsonify({'status' :'error', 'message' : 'Resource not found'}), 404
    
    @app.errorhandler(500)
    def server_error(e):
        return jsonify({'status' :'error', 'message' : 'Internal server error'}), 500

    return app

if __name__=='__main__':
    app = create_app()
    app.run(debug=True)