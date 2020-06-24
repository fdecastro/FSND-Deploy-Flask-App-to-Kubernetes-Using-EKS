FROM python:stretch

COPY . /flask_app
WORKDIR /flask_app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -U pytest

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "main:APP"]
