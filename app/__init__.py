#!/bin/env python3

"""
public routes
"""

# Flask is a class from the flask library
from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth
from dotenv import load_dotenv

load_dotenv()


# Initialize extensions (no app yet)
db = SQLAlchemy()
basic_auth = BasicAuth()  # from flask-admin extension
admin = Admin(name="microblog")  # app will be bound in create_app()


def create_app():
    # __call__ lets you make an instance behave like a function
    # app is WSGI applicatin
    app = Flask(__name__)  # Flask.__call__() 2 required postitional arguments
    import os

    # connection string constructor
    # driver is psycopg # python adapter psycopg
    # flask configutarion variable to tell the app which db should connect
    # dialect+driver://username:password@host:port/database # db dialect
    # \/// is a relative file path
    # Supabase database URI
    if callable(app):  # callable is a built-in function
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            f"postgresql+psycopg://{os.getenv('SUPABASE_DB_USER')}:"
            f"{os.getenv('SUPABASE_DB_PASSWORD')}@"
            f"{os.getenv('SUPABASE_DB_HOST')}:"
            f"{os.getenv('SUPABASE_DB_PORT')}/"
            f"{os.getenv('SUPABASE_DB_NAME')}"
        )

    # do not track object modifications. slows down the app
    # even though not importing models_commited
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # from flask_basicauth
    # connect to wsgi flask and then sign in to 127.0.0.1:9000
    app.config["BASIC_AUTH_USERNAME"] = "adminuser"
    app.config["BASIC_AUTH_PASSWORD"] = "password"

    # Initialize extensions
    db.init_app(app)
    basic_auth.init_app(app)

    from .models import Project

    # from flask-admin extension for admin panel
    admin.add_view(ModelView(Project, db.session))

    @app.route("/")  # REST endpoint
    def index():
        """Render public home page from db."""
        projects = Project.query.all()
        return render_template("index.html", projects=projects)

    @app.route("/projects/<int:project_id>")
    def project_detail(project_id):
        """Render db session detail per project id."""
        project = db.session.get(Project, project_id)
        if not project:
            abort(404)
        return render_template("detail.html", project=project)

    @app.route("/about")
    def about_me():
        """Render about me page template form."""
        return render_template("about.html")

    @app.errorhandler(404)
    def not_found(error):
        """Render custom page not found error."""
        return render_template("404.html", msg=error), 404

    from .routes import bp

    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()  # does not update current tables
    return app
