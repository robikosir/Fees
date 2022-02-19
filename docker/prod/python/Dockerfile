FROM python:3.7.0
ENV PYTHONUNBUFFERED 1
RUN mkdir /fees
WORKDIR /fees
COPY . /fees/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements/prod.txt
EXPOSE 8000
