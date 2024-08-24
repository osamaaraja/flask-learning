
from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123abc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


# dummy data
posts = [
    {
        'author': 'RajaNova',
        'title': 'Blog Post 1',
        'content': 'This is first post content',
        'date_posted': 'August 17,2024'

    },
    {
        'author': 'RajaVortex',
        'title': 'Blog Post 2',
        'content': 'This is second post content',
        'date_posted': 'August 27,2024'
    }
]

@app.route("/")
@app.route("/home")
def home():

    return render_template('home.html', posts=posts)

@app.route("/about")
def about():

    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'admin':
            flash(f"Logged in as {form.username}", "success")
            return redirect(url_for('home'))
        else:
            flash(f"Invalid Login or Password", "danger")
    return render_template('login.html', title='Log In', form=form)


if __name__=='__main__':
    app.run(debug=True)

