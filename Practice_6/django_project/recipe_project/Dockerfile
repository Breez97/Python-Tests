FROM python:3.9-slim

ENV DJANGO_SETTINGS_MODULE=recipe_project.settings

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install pytest pylint
RUN pylint recipe_project && pytest

CMD ["gunicorn", "-b", "0.0.0.0:8000", "recipe_project.wsgi:application"]