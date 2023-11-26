FROM python:3.9.18-alpine 

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV POSTGRES_PASSWORD=1234
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=sectionb
ENV DB_HOST=db_service


COPY . /app/



RUN pip install --upgrade pip && pip install -r requirements.txt 
   

EXPOSE 8000

#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["gunicorn", "SectionB.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]