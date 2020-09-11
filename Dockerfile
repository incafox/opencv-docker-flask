FROM python:3
ADD main.py /
RUN pip install flask
RUN pip install opencv-python
CMD ["env FLASK_APP=main.py flask run"]
