APP LINK:- https://bigmart-practise.herokuapp.com/

create env

activate the env

create a requirements.txt

install the requirements

git init

dvc init

dvc add data_given/train.csv

git add . && git commit -m "first commit" 

git branch -M main

git add . && git commit -m "docker added"  && git push origin main

git add . && git commit -m "docker added"  && git push origin mlflow


tox # Tox command

tox -r # Tox rebuild

pytest -v

pip install -e . # setup.py command

python setup.py sdist bdist_wheel #building your own packages

create an artifacts folder

mlflow server command - 
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 127.0.0.1 -p 8769


docker login
docker tag image:local_tag username/reponame:customtag
docker push username/imagename:customtag
