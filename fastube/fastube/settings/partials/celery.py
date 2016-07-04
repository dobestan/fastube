CELERY_ACCEPT_CONTENT = ['pickle', 'json']


# Using Redis
# http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html

BROKER_URL = 'redis://localhost:6379/0'
