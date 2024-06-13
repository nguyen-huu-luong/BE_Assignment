FROM python:3.9.0
WORKDIR /BE_Assignment
COPY ./requirements.txt .
COPY ./startup.sh .
RUN pip install -r requirements.txt
RUN chmod +x startup.sh
ENTRYPOINT [ "./startup.sh" ]