FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf

COPY ./docker/prod/nginx/django_fees.conf /etc/nginx/conf.d/
COPY ./docker/prod/nginx/ssl_django_fees.conf /etc/nginx/conf.d/
