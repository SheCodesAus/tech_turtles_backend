release: python presentpals/manage.py migrate
web: gunicorn --pythonpath presentpals presentpals.wsgi --log-file -