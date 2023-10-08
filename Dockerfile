FROM python:3.10-slim
#LABEL maintainer="cynthiahu3727@gmail.com"
COPY requirements.txt /app/
WORKDIR /app
RUN apt-get update
RUN apt-get -y install gcc
RUN apt-get install -y python3
RUN apt-get -y install python3-pip
RUN pip install -r requirements.txt
COPY base.html user.html index.html user.html /app/
COPY hello.py /app/
ENV FLASK_APP=hello.py

CMD [ "python", "-m", "flask" ,"run"]

# CMD ["python", "hello.py"]
#COPY requirements.txt /opt/app/requirements.txt
#WORKDIR /opt/app
#RUN pip install -r requirements.txt
#COPY . /opt/app