FROM python:3.10
ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install brokelads backend
WORKDIR /app
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
ADD backend /app

EXPOSE 8000