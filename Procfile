web: gunicorn -t 4 --keep-alive=5 otree.wsgi
worker: python manage.py celery worker --app=otree.celery.app:app --loglevel=INFO
