from . import celery
from datetime import datetime

@celery.task
def say_hello(name:str):
    print(f"Hello {name}! The time is {datetime.now()}")
    return "Hello {}!".format(name)
