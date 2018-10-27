FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN mv /code/project/medManage wellframe_challenge/
RUN cd wellframe_challenge && python manage.py makemigrations medManage && python manage.py migrate
