FROM python:3.10.6
ENV PYTHONUNBUFFERED=1

# set the working directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir

# copy source code to to /app folder
COPY . /app

# start the server
CMD [ "./manage.py", "runserver", "0.0.0.0:80" ]