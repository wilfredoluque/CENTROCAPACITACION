from flask import Flask
from config import Config
from models.database import create_tables
from controllers.auth_controller import bp as auth_controller
from controllers.dashboard_controller import bp as dashboard_controller
from controllers.estudiantes_controller import bp as estudiantes_controller
from controllers.cursos_controller import bp as cursos_controller
from controllers.inscripcion_controller import bp as inscripcion_controller
from controllers.usuarios_controller import bp as usuarios_controller

def create_app():
    app = Flask(__name__, template_folder='views', static_folder='static')
    app.config.from_object(Config)

    app.register_blueprint(auth_controller, url_prefix='/auth')
    app.register_blueprint(dashboard_controller)
    app.register_blueprint(estudiantes_controller, url_prefix='/estudiantes')
    app.register_blueprint(cursos_controller, url_prefix='/cursos')
    app.register_blueprint(inscripcion_controller, url_prefix='/inscripcion')
    app.register_blueprint(usuarios_controller, url_prefix='/usuarios')

    with app.app_context():
        create_tables()

    return app

# <- Aquí se crea la variable global 'app' que gunicorn necesita
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5002)
