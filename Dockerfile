FROM python:3.9
RUN apt-get update && apt-get install -y libpq-dev
RUN pip install psycopg2-binary
RUN pip install python-dotenv
RUN pip install django
COPY . /app  
WORKDIR /app 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]