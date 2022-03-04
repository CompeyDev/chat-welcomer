FROM python:3.8.12
WORKDIR app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
COPY chat-welcomer.py .
CMD python chat-welcomer.py
