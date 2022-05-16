from email.mime import application
from flask import Flask
from config import DevelopmentConfig

application = Flask(__name__)
application.config.from_object(DevelopmentConfig)

from core import routes
