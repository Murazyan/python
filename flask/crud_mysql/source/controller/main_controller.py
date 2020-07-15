
from flask import Flask, url_for, render_template, session
from sqlalchemy.exc import IntegrityError as sqla_IntegrityError, DatabaseError
from source.model_manager.user_manager import *
import source.models.entites as  entity

def def_control(app):

    @app.route('/')
    def hello_world():
        print('kanchvec index html')
        # return render_template('index.html')
        return render_template('index.html')

    # @app.route('/save_user')
    # def save_user():
    #     user = entity.User('Python','python@gmail.com','123456')
    #     entity.db.session.add(user)
    #     entity.db.session.commit()
    #     return True

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 404

    @app.errorhandler(DatabaseError)
    def special_exception_handler(error):
        return 'Database connection failed', 500

    @app.errorhandler(sqla_IntegrityError)
    def integrity_exception_handler(error_msg):
        msg = 'Error: Last names must be unique'
        return render_template('server_error.html', msg=msg), 500

    @app.errorhandler(AssertionError)
    def validation_exception_handler(error_msg):
        return render_template('server_error.html', msg=error_msg), 500

    @app.errorhandler(RuntimeError)
    def login_exception_handler(error_msg):
        msg = 'You are not logged in'
        return render_template('server_error.html', msg=msg), 500


