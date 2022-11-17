FROM python:3

RUN mkdir -p /tema10/
COPY . /tema10/
RUN pip install -r /tema10/Scripts/requirements.txt

WORKDIR /tema10/Scripts/

CMD ["python3","main.py"]


