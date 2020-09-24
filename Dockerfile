FROM python:3.8-buster

ENV WORKDIR="/opt/app"
WORKDIR ${WORKDIR}
COPY . ${WORKDIR}

RUN make init
