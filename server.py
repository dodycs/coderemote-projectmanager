from flask import Flask, flash, session, request, redirect, render_template, url_for

from db.data_layer import create_project, get_all_projects, get_project, update_project, delete_project
from db.data_layer import create_task, get_all_tasks, update_task, delete_task

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



app.run(debug=True)