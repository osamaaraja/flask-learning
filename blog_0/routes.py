import os
import secrets
from tkinter import Image

from blog_0.models import User, Post
from flask import render_template, flash, redirect, url_for, request, abort
from blog_0.forms import LoginForm, RegistrationForm, PostForm, RequestResetForm, ResetPasswordForm, UpdateAccountForm
from blog_0 import app, db, bcrypt, mail
from flask_login import login_user, logout_user, current_user, login_required
from flask_mail import Message
# dummy data
'''
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
'''
@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():

    return render_template('about.html', title='About')











