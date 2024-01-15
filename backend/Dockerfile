FROM python:3.11-slim
WORKDIR /backend
COPY ./requirements /backend/requirements
RUN pip install --no-cache-dir --upgrade -r /backend/requirements/requirements.txt
COPY ./app /backend/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]