web: gunicorn --keyfile=/otree/otree-core/certs/privkey.pem --certfile=/otree/otree-core/certs/cert.pem --ca-certs=/otree/otree-core/certs/chain.pem --ssl-version=3 --ciphers=TLSv1 otree.wsgi
worker: python manage.py celery worker --app=otree.celery.app:app --loglevel=INFO
