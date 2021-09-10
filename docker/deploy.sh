#!/bin/bash
git checkout master
echo '---------- Git checkout master complete ----------'
git fetch --all
echo '---------- Git fetch complete ----------'
git reset --hard origin/master
echo '---------- Git reset master complete ----------'
echo '---------- Docker compose build started ----------'
sudo docker-compose -f $1 build
echo '---------- Docker compose build complete ----------'
echo '---------- Docker compose deploy started ----------'
sudo docker-compose -f $1 up -d
echo '---------- Docker compose deploy complete ----------'
echo '---------- Docker compose migrate started ----------'
sudo sudo docker-compose -f $1 exec drf bash
sudo python manage.py migrate
echo '---------- Docker compose migrate complete ----------'
echo '---------- Docker compose collectstatic started ----------'
yes | python manage.py collectstatic --noinput
echo '---------- Docker compose collectstatic completed ----------'
