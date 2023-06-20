
FROM python:3.9


ENV SECRET_KEY="django-insecure-nw^y+m^wmxza1asgk+)!ua2qx9)g+#v=6%76-9i8i(6eqiw94j"
ENV DEBUG=False


COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt


RUN mkdir /site
COPY . /site
WORKDIR /site

EXPOSE 8000

RUN [ "python", "manage.py", "makemigrations"]
RUN [ "python", "manage.py", "migrate"]


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

