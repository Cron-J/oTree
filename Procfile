web: gunicorn --certfile=/otree/otree-core/certs/fullchain.pem --keyfile=/otree/otree-core/certs/privkey.pem otree.wsgi
worker: python manage.py celery worker --app=otree.celery.app:app --loglevel=INFO
