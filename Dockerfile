FROM python:3.7.0
ENV PYTHONUNBUFFERED 1
RUN mkdir /fees
WORKDIR /fees
COPY . /fees/
RUN pip install -r requirements.txt
EXPOSE 8000
