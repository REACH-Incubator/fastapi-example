FROM python:3

ADD . /source

ENTRYPOINT [ "/source/entrypoint.sh" ]