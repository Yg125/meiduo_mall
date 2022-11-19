from celery_tasks.cel import app


@app.task(bind=True)
def sum(self, num1, num2):
    return num1 + num2
