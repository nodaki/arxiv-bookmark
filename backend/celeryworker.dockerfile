FROM python:3.7

COPY ./app /app
WORKDIR /app/

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app

COPY ./app/worker-start.sh /worker-start.sh

RUN chmod +x /worker-start.sh

CMD ["bash", "/worker-start.sh"]