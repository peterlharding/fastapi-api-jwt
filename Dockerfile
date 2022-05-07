
FROM python:3.9.10-slim-bullseye

ENV AWS_DEFAULT_REGION=ap-southeast-2

ARG PY_TRUSTED="--trusted-host pypi.python.org  --trusted-host pypi.org  --trusted-host files.pythonhosted.org"

COPY ./requirements.txt /tmp/requirements.txt

RUN python -m pip install -q $PY_TRUSTED --upgrade pip && \
    python -m pip install $PY_TRUSTED -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt

ADD ./src /src

EXPOSE 8000

WORKDIR /

ADD .env /

CMD [ "/src/scripts/run.sh" ]
# CMD sleep 5000

