from flask import Flask

#initialize the app
app = Flask(__name__,instance_relative_config=True)

#Loads the views
from app import views

#Load the config file
app.config.from_object('config')
