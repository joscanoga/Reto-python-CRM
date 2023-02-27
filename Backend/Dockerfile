# Create our image based on Python 3.10
FROM python:3.10

# Expose ports
EXPOSE 8000

# Tell Python to not generate .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Turn off buffering
ENV PYTHONUNBUFFERED 1

# Install requirements using pip
ADD requirements.txt .
RUN python -m pip install -r requirements.txt



# Set working directory and addour django API files
WORKDIR /app
ADD . .
RUN python manage.py migrate
RUN python  cliente.py
CMD python manage.py runserver