FROM python:3

ADD . /source
RUN pip install -r /source/requirements.txt

ENTRYPOINT [ "/source/entrypoint.sh" ]