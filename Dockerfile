FROM python:3.8-alpine
RUN mkdir /app
ADD . /app
WORKDIR /app
CMD ["python", "debug-in-docker-demo-1.py"]