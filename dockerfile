FROM python:3-alpine3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 80
CMD [ "python", "./app.py" ]