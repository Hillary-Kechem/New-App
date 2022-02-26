from flask import Flask
from .config import Devconfig

#initialising application
app = Flask(__name__, instance_relative_config = True)

#Setting up configuratiion 
app.config.from_object(Devconfig)
app.config.from__pyfile('config.py')


from app import views
