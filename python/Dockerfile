FROM python:3-onbuild
WORKDIR /usr/src/app
ADD ./hello.py /usr/src/app
ADD ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt
CMD ["python", "./hello.py"]
