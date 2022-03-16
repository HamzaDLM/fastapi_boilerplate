from celery import Celery


celery = Celery(__name__)

celery.conf.update(
    result_expires=60,
    task_acks_late=True,
    broker_url="",
    result_backend=""
)


@celery.task(name="example task")
def task():
    pass