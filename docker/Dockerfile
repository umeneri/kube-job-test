FROM python:3.7-alpine

WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app
CMD python gcs.py create_object
# CMD while :; do date; sleep 1; done
