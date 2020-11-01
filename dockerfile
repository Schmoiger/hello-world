FROM python:3

# set a directory for the app
WORKDIR /hello-world

# copy all the files to the container
COPY . /hello-world

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN ["pytest", "-v", "--junitxml=reports/result.xml"]

CMD tail -f /dev/null
