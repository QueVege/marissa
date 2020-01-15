from marissa.celery_app import app


@app.task(name='add_to_db')
def add_to_db():
    pass