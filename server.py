from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from random import choice


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route('/')
def start_here():
    """Home page."""

    return render_template("index.html")



@app.route('/application-form')
def show_form():
    """Show application form to user."""


    jobs = ["Software Engineer", "QA Engineer", "Product Manager"]


    return render_template("application-form.html", jobs= jobs)



@app.route('/application-success')
def show_success():
    """Show application success with items passed from form."""

    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    salary_basic = float(request.args.get("salary"))
    salary = '${:,.2f}'.format(salary_basic)
    job = request.args.get("job")
 


    return render_template("application-response.html",
                           firstname= firstname, 
                           lastname= lastname, 
                           salary=salary,
                           job=job
                           )



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
