#!/bin/env python3

"""
blueprint using admin
basic_auth /admin routes
"""

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    abort,
)
from .models import Project
from datetime import datetime
from . import basic_auth, db

# factor an app into a set of blueprints
# instantiate an app object
# initialize severl extensions
# register a collectin of blueprints
# main is the bp name.
# every route in a bp automatically has its endpoint prefixed with the bp name
# if templates change place add a templates_folder **kwrds argument
bp = Blueprint(
    "main",  # rename html template url_for
    __name__,
)


@bp.route("/admin/projects/new", methods=["GET", "POST"])
@basic_auth.required
def add_project():
    """Render admin new project form html.
    does not require application context
    flask automatically does it when pushing and handling a request"""

    if request.method == "POST":
        year_and_month = request.form.get("date")
        # model takes datetimeobject in column
        convert_string = datetime.strptime(year_and_month, "%Y-%m").date()

        new_project = Project(
            # get is a dictionary method needs parentheses
            title=request.form.get("title"),
            created=convert_string,
            description=request.form.get("desc"),
            skills=request.form.get("skills"),
            github_repo=request.form.get("github"),
        )

        db.session.add(new_project)
        db.session.commit()
        # main.index is bp does not exist in bp
        return redirect(url_for("index"))
    return render_template("projectform.html")


@bp.route("/admin/projects/<int:project_id>/edit", methods=["GET", "POST"])
@basic_auth.required
def project_edit(project_id):
    """Render edition page for admin with same conventions from add project."""
    """does not require application context
    # flask automatically does it when pushing and handling a request"""
    project = db.session.get(Project, project_id)

    #    project = Project.query.get_or_404(project_id)
    if not project:
        abort(404)  # not found

    if request.method == "POST":

        # date is nullable=False
        year_and_month = request.form.get("date")
        if not year_and_month:
            abort(400)  # bad request
        convert_string = datetime.strptime(year_and_month, "%Y-%m").date()

        project.title = request.form.get("title")
        project.created = convert_string
        project.description = request.form.get("desc")
        project.skills = request.form.get("skills")
        project.github_repo = request.form.get("github")
        db.session.commit()
        return redirect(url_for("index"))  # main.index exists in bp?

    return render_template("editform.html", project=project)


@bp.route("/admin/projects/<int:project_id>/delete")
@basic_auth.required
def project_delete(project_id):
    """Delete project from db and redirect to home."""
    """does not require application context
    flask automatically does it when pushing and handling a request"""

    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("index"))
