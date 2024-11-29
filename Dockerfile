FROM python:3.11

EXPOSE 8080
WORKDIR /app

# Important: you are making a copy and putting it in the folder /app. None of the changes
# that you make in your repository, folders, or host machine drive will make it into this
# copy.
COPY . ./

RUN pip install -r requirements.txt

# Starts up streamlit, whenever you type docker run. You can subsequently exec into it.
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
