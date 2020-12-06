FROM python:3.7

WORKDIR /home/

ENV FLASK_APP=webapp.py

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python","webapp.py"]