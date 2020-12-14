FROM python:3.7

WORKDIR /home/

ENV FLASK_APP=webapp.py

COPY requirements.txt requirements.txt

COPY import_nltk.py import_nltk.py

RUN pip install -r requirements.txt

RUN python import_nltk.py

COPY . .

EXPOSE 5000

CMD ["python","webapp.py"]
