#Base Image to use
FROM python:3.10.10-slim-buster
# FROM python:3.7.9-slim

#Expose port 8080
EXPOSE 8080

#Copy Requirements.txt file into app directory
COPY requirements.txt app/requirements.txt

# RUN echo export SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL = True
#install all requirements in requirements.txt
RUN pip install -r app/requirements.txt

#Copy all files in current directory into app directory
COPY . /app

# COPY /src /app/src

#Change Working Directory to app directory
WORKDIR /app

#Run the application on port 8080
# ENTRYPOINT ["streamlit", "run", "app2.py", "--server.port=8080", "--server.address=0.0.0.0"]
ENTRYPOINT ["python", "OOP.py"]