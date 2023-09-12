# container based on python
FROM python:3.9
# 
ENV PYTHONUNBUFFERED 1
# create a folder that will have the container
RUN mkdir /app

RUN ["echo", "help"]
# work directory for all project files to exist
WORKDIR /app
# install modules and dependencies
COPY requirements.txt /app/
# install the requirements
RUN pip install -r requirements.txt
# copy the folder from vs code to the container in the app folder
COPY . /app/

CMD ["python", "mongo_init.py"]

RUN ["echo", "help"]