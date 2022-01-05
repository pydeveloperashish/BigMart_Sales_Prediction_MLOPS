FROM python:3.7
COPY . usr/app/
#EXPOSE 5000 heroku doesnt need this to deploy through docker
WORKDIR /usr/app
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN apt-get update -y && apt-get install -y gcc
RUN pip install -r requirements.txt --ignore-installed
CMD python app.py