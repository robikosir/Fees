#!/bin/bash
sudo echo '---------- Removing old Docker images ----------'
sudo yes | docker image prune -a
sudo echo '---------- Removing old Docker images completed ----------'
sudo git checkout master
sudo echo '---------- Git checkout master complete ----------'
sudo git fetch --all
sudo echo '---------- Git fetch complete ----------'
sudo git reset --hard origin/master
sudo echo '---------- Git reset master complete ----------'
sudo echo '---------- Docker compose build started ----------'
sudo docker-compose -f $1 build
sudo echo '---------- Docker compose build complete ----------'
sudo echo '---------- Docker compose deploy started ----------'
sudo docker-compose -f $1 up -d
sudo echo '---------- Docker compose deploy complete ----------'
sudo echo '---------- Docker compose migrate --run-syncdb started ----------'
sudo docker exec -it django_rest bash
python manage.py migrate --run-syncdb
python manage.py collectstatic --noinput
exit
sudo echo '---------- Deploy.sh completed ----------'
sudo git rev-parse HEAD
