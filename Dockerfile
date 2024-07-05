FROM python:3.11

WORKDIR /api

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . . 

# CMD ["gunicorn", "design.wsgi:application", "--bind", "0.0.0.:8002"]
RUN chmod +x ./entrypoint.sh
# ENTRYPOINT ["python manage.py runserver 0.0.0.0:8002"]
