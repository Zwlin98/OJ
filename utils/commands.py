# celery -A OJ beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
# celery -A OJ worker -l info
# celery -A OJ worker -l info; celery -A OJ beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler