from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add", methods=['GET'])
def student_add():
    """Add a student."""

    return render_template("student_add.html")


@app.route("/student-add-confirmation", methods=['POST'])
def student_add_confirmation():
    """Confirm student has been added."""

    first = request.form.get('firstname')
    last = request.form.get('lastname')
    github = request.form.get('github')
    hackbright.make_new_student(first, last, github)

    return render_template("student_add_confirmation.html",
                            github=github)

# # Keeps /student-add route, but two methods based on form submission
# @app.route("/student-add", methods=['POST'])
# def display_student_add():
#     """Display student info."""

#     first = request.form.get('firstname')
#     last = request.form.get('lastname')
#     github = request.form.get('github')
#     hackbright.make_new_student(first, last, github)

#     return render_template("student_info.html",
#                            first=first,
#                            last=last,
#                            github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
