from flask import Flask, render_template, flash
from forms import LoginForm, RegistrationForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '123abc'
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
        flash(f"Account created for {form.username.data}!")

    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__=='__main__':
    app.run(debug=True)

