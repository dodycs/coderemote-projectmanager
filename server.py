from flask import Flask, flash, session, request, redirect, render_template, url_for

from db.data_layer import create_project, get_all_projects, get_project, update_project, delete_project
from db.data_layer import create_task, get_all_tasks, get_task, update_task, delete_task

app = Flask(__name__)

# PROJECT
@app.route('/')
def project_index():
    projects = get_all_projects()
    return render_template('project/index.html', projects = projects)

@app.route('/project/add', methods=['POST'])
def add_project():
    try:
        title = request.form['title']
        create_project(title)
    except:
        pass
    return redirect(url_for('project_index'))

@app.route('/project/delete/<project_id>')
def remove_project(project_id):
    delete_project(project_id)
    return redirect(url_for('project_index'))

@app.route('/project/edit/<project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
    if request.method == 'POST':
        try:
            update_project(project_id, request.form['title'])
        except:
            pass
        return redirect(url_for('project_index'))

    project = get_project(project_id)
    return render_template('project/show.html', project = project)

# TASK
@app.route('/project/<project_id>/tasks')
def task_index(project_id):
    project = get_project(project_id)
    return render_template('task/index.html', project = project)

@app.route('/project/<project_id>/task/add', methods=['POST'])
def add_task(project_id):
    try:
        description = request.form['description']
        create_task(project_id, description)
    except:
        raise
    return redirect(url_for('task_index', project_id = project_id))

@app.route('/project/<project_id>/task/<task_id>/delete')
def remove_task(project_id, task_id):
    delete_task(task_id)
    return redirect(url_for('task_index', project_id = project_id))

@app.route('/project/<project_id>/task/<task_id>/edit/', methods=['GET', 'POST'])
def edit_task(project_id, task_id):
    if request.method == 'POST':
        try:
            update_task(task_id, request.form['description'])
        except:
            pass
        return redirect(url_for('task_index', project_id = project_id))

    task = get_task(task_id)
    return render_template('task/show.html', task = task)

app.run(debug=True)