FROM nginx:stable

RUN rm /etc/nginx/conf.d/default.conf

COPY ./docker/prod/nginx/django_fees.conf /etc/nginx/conf.d/
COPY ./docker/prod/nginx/ssl_django_fees.conf /etc/nginx/conf.d/

RUN  apt-get update \
      && apt-get install -y cron certbot python-certbot-nginx bash wget \
      && certbot certonly --standalone --agree-tos -m "robikoser@gmail.com" -n -d "34.141.81.19" \
      && rm -rf /var/lib/apt/lists/* \
      && echo "PATH=$PATH" > /etc/cron.d/certbot-renew  \
      && echo "@monthly certbot renew --nginx >> /var/log/cron.log 2>&1" >>/etc/cron.d/certbot-renew \
      && crontab /etc/cron.d/certbot-renew



VOLUME /etc/letsencrypt


CMD [ "sh", "-c", "cron && nginx -g 'daemon off;'" ]
