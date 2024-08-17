from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__=='__main__':
    app.run(debug=True)

