import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from source.controller import main_controller

PWD = os.getcwd()

template_folder = os.path.join(PWD, "source/resources/templates/")
static_folder = os.path.join(PWD, "source/resources/static/")


app = Flask(__name__,
                  template_folder=template_folder,
                  static_folder=static_folder)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost:3306/events_tracker?useSSL=false&useUnicode=yes&characterEncoding=UTF-8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:devm@localhost:3306/events_tracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
sqldb = SQLAlchemy()
sqldb.init_app(app)
main_controller.def_control(app)


if __name__ == '__main__':
    app.run()
