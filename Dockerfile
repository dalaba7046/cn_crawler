# 
FROM python:3.10.8-slim 

# 
ENV PYTHONUNBUFFERED True

ENV APP_HOME /code
WORKDIR $APP_HOME
# 
COPY . ./
# 
RUN pip install --no-cache-dir -r requirements.txt

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
