from db.base import DbManager
from db.entities import Project, Task



# PROJECT FUNCTIONS

def get_project(project_id):
    db = DbManager()
    return db.open().query(Project).filter(Project.id == project_id).one()

def get_all_projects():
    db = DbManager()
    return db.open().query(Project).all()

def create_project(title):
    db = DbManager()
    project = Project()
    project.title = title
    return db.save(project)

def update_project(project_id, title):
    db = DbManager()
    project = db.open().query(Project).filter(Project.id == project_id).one()
    project.title = title
    return db.update(project)

def delete_project(project_id):
    db = DbManager()
    project = db.open().query(Project).filter(Project.id == project_id).one()
    project = db.delete(project)
    db.close()
    return project


# TASK FUNCTIONS

def create_task(project_id, description):
    db = DbManager()
    task = Task()
    task.description = description
    task.project_id = project_id
    return db.save(task)

def get_task(task_id):
    db = DbManager()
    return db.open().query(Task).filter(Task.id == task_id).one()

def get_all_tasks(project_id):
    db = DbManager()
    return db.open().query(Task).filter(Task.project_id == project_id).all()

def update_task(task_id, description):
    db = DbManager()
    task = db.open().query(Task).filter(Task.id == task_id).one()
    task.description = description
    return db.update(task)

def delete_task(task_id):
    print('-------------------------------------------')
    print(task_id)
    db = DbManager()
    task = db.open().query(Task).filter(Task.id == task_id).one()
    task = db.delete(task)
    db.close()
    return task