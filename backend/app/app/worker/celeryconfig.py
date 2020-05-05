import os

broker_url = os.getenv("BROKER_URL", "amqp://localhost")
result_backend = os.getenv("CELERY_RESULT_BACKEND", "rpc://")
include = ["app.worker.tasks"]
