FROM python:3.11

EXPOSE 8080

ENV ROOT_DIR=/tarefa_1

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=$PYTHONPATH:$ROOT_DIR

WORKDIR $ROOT_DIR

COPY requirements.txt $ROOT_DIR

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . $ROOT_DIR

CMD ["python", "job_task1.py"]