FROM python:3.4-slim
MAINTAINER Raul Speroni (raulsperoni@gmail.com)


# Export env settings
ENV TERM=xterm
ENV LANG en_US.UTF-8

RUN pip install -U pip
RUN pip install spacy
RUN python -m spacy download es
COPY libs/ /krypton/
WORKDIR /krypton


 CMD ["python", "-u", "nerTaggerServer.py"]




