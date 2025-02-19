@@ -0,0 +1,7 @@
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install fastapi uvicorn python-multipart
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000
