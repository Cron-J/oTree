web: gunicorn -t 4 --keep-alive=5 --forwarded-allow-ips=gxpapp_nginx_1.gxpapp_gxp otree.wsgi
worker: python manage.py celery worker --app=otree.celery.app:app --loglevel=INFO
