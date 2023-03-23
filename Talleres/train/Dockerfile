FROM python:3.9
RUN mkdir /train
WORKDIR /train
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install jupyter==1.0.0 -U && pip install jupyterlab==3.6.1
EXPOSE 8080
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
#EXPOSE 8888
#ENTRYPOINT ["jupyter", "lab","--ip=0.0.0.0","--allow-root"]
