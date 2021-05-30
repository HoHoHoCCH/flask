from flask import Flask, render_template

from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learning-git')
def learning_git():
    return render_template('git.html')

