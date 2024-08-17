from flask import Flask
app = Flask(__name__)

'''
for running 
-> Option #1:
set the following environment variables
FLASK_APP=basic_setup.py;FLASK_DEBUG=1

-> Option #2:
the script can be run directly by defining 
a conditional at the end of the script -> if __name__=='__main__':app.run(debug=True)
'''

@app.route("/")
@app.route("/home")
def home():

    return "<h1>Home Page</h1>"

@app.route("/about")
def about():

    return "<h1>About Page!</h1>"

if __name__=='__main__':
    app.run(debug=True)