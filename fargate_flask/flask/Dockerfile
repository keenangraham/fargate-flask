FROM python:3.8-slim-buster

EXPOSE 80

ENV VIRTUAL_ENV=/opt/venv

RUN apt-get update

RUN apt-get install make git -y

RUN python -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python -m pip install --upgrade pip

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["make", "prod"]