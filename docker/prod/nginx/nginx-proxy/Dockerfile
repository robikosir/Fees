FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf

COPY ./docker/prod/nginx/nginx-proxy/nginx.conf /etc/nginx/conf.d/
