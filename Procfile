web: gunicorn business_course.wsgi --log-file -
worker: celery -A business_course worker -l info
beat: celery -A business_course beat -l info
