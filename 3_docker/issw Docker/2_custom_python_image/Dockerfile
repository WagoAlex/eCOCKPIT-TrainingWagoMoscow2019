FROM python:3.6-slim

LABEL maintainer <>.<>@wago.com
RUN pip install requests
COPY . .
EXPOSE 8080 
CMD ["python3","script.py"] # when container ist started execute "python3 script.py"
