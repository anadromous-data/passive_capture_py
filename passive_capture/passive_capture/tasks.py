from __future__ import absolute_import, unicode_literals
from .celery import app

@app.task
def add(x, y):
    return x + y

@app.task
def conkat(x, y):
    return x + y