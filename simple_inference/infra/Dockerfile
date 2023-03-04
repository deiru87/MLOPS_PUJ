FROM python:3.9
# set work directory
WORKDIR /app

COPY . .
RUN pip3 install --no-cache-dir --upgrade -r infra/requirements.txt

CMD ["uvicorn", "app.src.service.inference_service:app", "--host", "0.0.0.0", "--port", "80"]