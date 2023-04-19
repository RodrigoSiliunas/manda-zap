from flask import Flask
from flask_jwt_extended import JWTManager

from app.config.database import db
from app.config.configuration import DevelopmentConfig

from .routes.teachers.index import bp as teachers
from .routes.students.index import bp as students

"""
==========================================================================
 ➠ Section By: Rodrigo Siliunas (Rô: https://github.com/RodrigoSiliunas)
 ➠ Related system: Core
==========================================================================
"""

app = Flask(__name__)
jwt = JWTManager(app)

# Puxamos as configurações de um objeto.
app.config.from_object(DevelopmentConfig)

# Instancia do MongoEngine.
db.init_app(app)


"""
==========================================
 ➠ Section: Blueprints Registry
==========================================
"""
app.register_blueprint(teachers)
app.register_blueprint(students)
